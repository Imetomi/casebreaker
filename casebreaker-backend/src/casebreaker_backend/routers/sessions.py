from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List, AsyncGenerator
from datetime import datetime

from ..database import get_db
from ..models import Session as SessionModel, CaseStudy as CaseStudyModel, ChatMessage as ChatMessageModel
from ..schemas import Session, SessionCreate, ChatMessage, ChatMessageCreate
from ..services.claude import claude_service

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"]
)

@router.post("/", response_model=Session)
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
    # Verify case study exists
    case_study = db.query(CaseStudyModel).filter(CaseStudyModel.id == session.case_study_id).first()
    if not case_study:
        raise HTTPException(status_code=404, detail="Case study not found")
    
    db_session = SessionModel(**session.model_dump())
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
    session_id: int,
    message: ChatMessageCreate,
    db: Session = Depends(get_db)
):
    # Verify session exists
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Save user message
    db_message = ChatMessageModel(
        **message.model_dump(),
        session_id=session_id,
        timestamp=datetime.utcnow()
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

    # Get case study and checkpoint info
    case_study = session.case_study
    checkpoint = next(
        (cp for cp in case_study.checkpoints if cp["id"] == message.checkpoint_id),
        None
    ) if message.checkpoint_id else None

    if not checkpoint:
        raise HTTPException(status_code=400, detail="Invalid checkpoint ID")

    # Stream the AI response
    async def generate_and_save_response() -> AsyncGenerator[str, None]:
        response_content = ""
        async for chunk in claude_service.generate_response(
            messages=messages,
            case_study=case_study.__dict__,
            checkpoint=checkpoint
        ):
            response_content += chunk
            yield chunk

        # Save the complete AI response
        ai_message = ChatMessageModel(
            role="assistant",
            content=response_content,
            session_id=session_id,
            checkpoint_id=message.checkpoint_id,
            timestamp=datetime.utcnow()
        )
        db.add(ai_message)
        db.commit()

    return StreamingResponse(
        generate_and_save_response(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "text/event-stream"
        }
    )

@router.get("/{session_id}/messages", response_model=List[ChatMessage])
def list_chat_messages(session_id: int, db: Session = Depends(get_db)):
    # Verify session exists
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return db.query(ChatMessageModel).filter(ChatMessageModel.session_id == session_id).all()

@router.patch("/{session_id}/complete-checkpoint")
def complete_checkpoint(session_id: int, checkpoint_id: str, db: Session = Depends(get_db)):
    db_session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    
    completed = db_session.completed_checkpoints or []
    if checkpoint_id not in completed:
        completed.append(checkpoint_id)
        db_session.completed_checkpoints = completed
        db.commit()
    
    return {"message": "Checkpoint completed"}
