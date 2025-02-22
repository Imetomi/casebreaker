from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field as PydanticField


class FieldBase(BaseModel):
    name: str
    description: str | None = None
    icon_url: str | None = None


class FieldCreate(FieldBase):
    pass


class Field(FieldBase):
    id: int

    class Config:
        from_attributes = True


class SubtopicBase(BaseModel):
    name: str
    description: str | None = None
    field_id: int


class SubtopicCreate(SubtopicBase):
    pass


class Subtopic(SubtopicBase):
    id: int
    field: Field
    case_count: int = 0

    class Config:
        from_attributes = True
        json_encoders = {property: lambda x: x}


class CaseStudyBase(BaseModel):
    title: str
    description: str | None = None
    difficulty: int = PydanticField(ge=1, le=5)
    specialization: str | None = None
    learning_objectives: List[str] = []
    context_materials: Dict[str, Any] = {}
    checkpoints: List[Dict[str, Any]] = []
    source_url: str | None = None
    source_type: str = "GENERATED"
    subtopic_id: int
    estimated_time: int = PydanticField(ge=5, le=240)  # Time in minutes, between 5min and 4hrs


class CaseStudyCreate(CaseStudyBase):
    pass


class CaseStudy(CaseStudyBase):
    id: int
    share_slug: str
    last_updated: datetime
    created_at: datetime
    subtopic: Subtopic

    class Config:
        from_attributes = True


class ChatMessageBase(BaseModel):
    role: str = PydanticField(pattern="^(user|assistant)$")
    content: str
    checkpoint_id: str | None = None


class ChatMessageCreate(ChatMessageBase):
    pass


class ChatMessage(ChatMessageBase):
    id: int
    session_id: int
    timestamp: datetime

    class Config:
        from_attributes = True


class SessionBase(BaseModel):
    case_study_id: int
    device_id: str
    completed_checkpoints: List[str] = []
    status: str = "active"


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    id: int
    start_time: datetime
    case_study: CaseStudy
    chat_messages: List[ChatMessage] = []

    class Config:
        from_attributes = True
