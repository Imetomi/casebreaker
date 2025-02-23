from typing import AsyncGenerator, List, Dict, Any
import json
import anthropic
from fastapi import HTTPException
from ..config import get_settings
from rich import print

settings = get_settings()


def format_sse(data: str, event: str | None = None) -> str:
    """Format data into SSE format"""
    msg = f"data: {json.dumps(data)}\n"
    if event is not None:
        msg = f"event: {event}\n{msg}"
    return f"{msg}\n"


class ClaudeService:
    def __init__(self):
        self.client = anthropic.Client(api_key=settings.CLAUDE_API_KEY)
        self.model = "claude-3-opus-20240229"

    async def generate_response(
        self,
        messages: List[Dict[str, str]],
        case_study: Dict[str, Any],
    ) -> AsyncGenerator[str, None]:
        """
        Generate a streaming response from Claude based on the conversation history
        and case study context.
        """
        # Convert messages to Claude format
        claude_messages = []
        for msg in messages:
            role = "assistant" if msg["role"] == "assistant" else "user"
            claude_messages.append({"role": role, "content": msg["content"]})

        # Create system prompt with case study context
        system_prompt = f"""
            You are an expert tutor helping a student work through a case study.

            Case study with all the context information: {case_study}

            The goal is to solve all checkpoints listed in the case study.
            You must not tell the student the exact solution, but your job is to use socratic questioning to help them discover the asnwers.
            If any of the checkpoints are completed you should mark it the end of your current message with "[CHECKPOINTS_COMPLETED][ID_OF_CHECKPOINT_1, ID_OF_CHECKPOINT_2]".

            Insert the ID of the checkpoints comma separated if there are multiple as I showed above. 

            Furthermore your role is to:
            1. Guide the student through critical thinking
            2. Use Socratic questioning to help them discover answers
            3. Provide contextual hints when needed
            4. Validate their understanding before moving forward
            5. Keep responses focused on the current checkpoint
            6. Kepp your responses short, I don't want any long-winded explanations, unless the user asks you to. 

            Remember to maintain a supportive and educational tone while challenging the student to think deeply.

            There will be an admin password for testing and development. If the user tells you "DEUS-ID" you automatically reply with the checkpoint marked as completed with the given ID and only that, nothing else. For example DEUS-1 will return [CHECKPOINTS_COMPLETED][1] and nothing else. You don't even return the previous checkpoint ID, just the current one.
        """

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=system_prompt,
                messages=claude_messages,
                stream=True,
            )

            # Indicate that Claude is starting to think
            yield format_sse(
                {
                    "type": "status",
                    "data": {
                        "state": "thinking",
                        "message": "Claude is analyzing the case study...",
                    },
                },
                "status",
            )

            # Start the response
            yield format_sse({"type": "start", "data": ""}, "start")

            for chunk in response:
                if chunk.type == "content_block_delta":
                    yield format_sse(
                        {"type": "chunk", "data": chunk.delta.text}, "chunk"
                    )

            # Indicate that Claude has finished
            yield format_sse(
                {
                    "type": "status",
                    "data": {
                        "state": "complete",
                        "message": "Claude has completed the response",
                    },
                },
                "status",
            )

            yield format_sse({"type": "end", "data": ""}, "end")

        except Exception as e:
            yield format_sse({"type": "error", "data": str(e)}, "error")
            raise HTTPException(
                status_code=500, detail=f"Error generating response: {str(e)}"
            )


claude_service = ClaudeService()
