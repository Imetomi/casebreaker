from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List, AsyncGenerator
from datetime import datetime
import json
from ..services.claude import claude_service, format_sse

from ..database import get_db, SessionLocal
from ..models import (
    Session as SessionModel,
    CaseStudy as CaseStudyModel,
    ChatMessage as ChatMessageModel,
)
from ..schemas import Session, SessionCreate, ChatMessage, ChatMessageCreate
from ..services.claude import claude_service

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("/", response_model=Session)
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
    # Verify case study exists
    case_study = (
        db.query(CaseStudyModel)
        .filter(CaseStudyModel.id == session.case_study_id)
        .first()
    )
    if not case_study:
        raise HTTPException(status_code=404, detail="Case study not found")

    # Create session data with empty completed_checkpoints list
    session_data = session.model_dump()
    session_data["completed_checkpoints"] = []
    db_session = SessionModel(**session_data)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


@router.get("/", response_model=List[Session])
def list_sessions(device_id: str | None = None, db: Session = Depends(get_db)):
    query = db.query(SessionModel)
    if device_id:
        query = query.filter(SessionModel.device_id == device_id)
    return query.all()


@router.get("/{session_id}", response_model=Session)
def get_session(session_id: int, db: Session = Depends(get_db)):
    db_session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return db_session


@router.post("/{session_id}/messages")
async def create_chat_message(
    session_id: int, message: ChatMessageCreate, db: Session = Depends(get_db)
):
    # Verify session exists
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Save user message
    db_message = ChatMessageModel(
        **message.model_dump(), session_id=session_id, timestamp=datetime.utcnow()
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    # Get conversation history
    messages = [
        {"role": msg.role, "content": msg.content}
        for msg in db.query(ChatMessageModel)
        .filter(ChatMessageModel.session_id == session_id)
        .order_by(ChatMessageModel.timestamp)
        .all()
    ]

    # Create a new database session for the async generator
    async_db = SessionLocal()
    case_study = session.case_study

    # Stream the AI response
    async def generate_and_save_response():
        response_content = ""
        try:
            print("Starting response generation...")
            async for chunk in claude_service.generate_response(
                messages=messages,
                case_study={
                    "title": case_study.title,
                    "description": case_study.description,
                    "learning_objectives": case_study.learning_objectives,
                    "context_materials": case_study.context_materials,
                    "checkpoints": case_study.checkpoints,
                },
            ):
                yield chunk
                # Extract content from chunk if it's a text chunk
                try:
                    # Extract the data line from the SSE chunk
                    lines = chunk.strip().split("\n")
                    data_line = next(
                        (line for line in lines if line.startswith("data: ")), None
                    )
                    if data_line:
                        # Remove 'data: ' prefix
                        data_str = data_line.replace("data: ", "", 1).strip()
                        data = json.loads(data_str)
                        if data["type"] == "chunk":
                            chunk_content = data["data"]
                            response_content += chunk_content
                            print(
                                f"Accumulated content length: {len(response_content)}"
                            )

                            # Check for completed checkpoints marker
                            if "[CHECKPOINTS_COMPLETED]" in response_content:
                                import re

                                # Extract checkpoint IDs from the marker
                                match = re.search(
                                    r"\[CHECKPOINTS_COMPLETED\]\[([^\]]+)\]",
                                    response_content,
                                )
                                print(match)
                                if match:
                                    # Get the comma-separated checkpoint IDs
                                    checkpoint_ids = [
                                        id.strip() for id in match.group(1).split(",")
                                    ]

                                    # Remove the marker from response
                                    response_content = re.sub(
                                        r"\[CHECKPOINTS_COMPLETED\]\[[^\]]+\]",
                                        "",
                                        response_content,
                                    ).strip()

                                    # Update completed checkpoints in session
                                    completed = session.completed_checkpoints or []
                                    for checkpoint_id in checkpoint_ids:
                                        if checkpoint_id not in completed:
                                            completed.append(checkpoint_id)

                                    session.completed_checkpoints = completed
                                    db.commit()
                                    print(
                                        f"Checkpoints {checkpoint_ids} marked as completed"
                                    )
                                    print(session.completed_checkpoints)
                except Exception as e:
                    print(f"Error parsing chunk: {str(e)}")
                    print(f"Raw chunk: {chunk}")
                    pass

            print(f"Final response content length: {len(response_content)}")
            # Only save if we accumulated some content
            if response_content:
                print("Saving assistant message...")
                ai_message = ChatMessageModel(
                    role="assistant",
                    content=response_content,
                    session_id=session_id,
                    timestamp=datetime.utcnow(),
                )
                async_db.add(ai_message)
                async_db.commit()
                print("Assistant message saved successfully")
            else:
                print("No content accumulated, skipping save")

        except Exception as e:
            print(f"Error generating response: {str(e)}")
            error_msg = format_sse(
                {"type": "error", "data": f"Error generating response: {str(e)}"},
                "error",
            )
            yield error_msg
        finally:
            async_db.close()

    return StreamingResponse(
        generate_and_save_response(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "text/event-stream",
        },
    )


@router.get("/{session_id}/messages", response_model=List[ChatMessage])
def list_chat_messages(session_id: int, db: Session = Depends(get_db)):
    # Verify session exists
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    return (
        db.query(ChatMessageModel)
        .filter(ChatMessageModel.session_id == session_id)
        .all()
    )


@router.post("/{session_id}/checkpoints/{checkpoint_id}")
def complete_checkpoint(
    session_id: int, checkpoint_id: str, db: Session = Depends(get_db)
):
    # Get session and verify it exists
    db_session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    # Get case study and verify checkpoint exists
    case_study = db_session.case_study
    checkpoint_exists = any(cp["id"] == checkpoint_id for cp in case_study.checkpoints)
    if not checkpoint_exists:
        raise HTTPException(
            status_code=404, detail="Checkpoint not found in case study"
        )

    # Update completed checkpoints
    completed = db_session.completed_checkpoints or []
    if checkpoint_id not in completed:
        completed.append(checkpoint_id)
        db_session.completed_checkpoints = completed
        db.commit()

    return {"message": "Checkpoint completed", "completed_checkpoints": completed}
