from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from .mixins import JSONEncodedDict

class Base(DeclarativeBase):
    pass

class Field(Base):
    __tablename__ = "fields"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    icon_url = Column(String)
    
    subtopics = relationship("Subtopic", back_populates="field")

class Subtopic(Base):
    __tablename__ = "subtopics"
    
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey("fields.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    
    field = relationship("Field", back_populates="subtopics")
    case_studies = relationship("CaseStudy", back_populates="subtopic")

class CaseStudy(Base):
    __tablename__ = "case_studies"
    
    id = Column(Integer, primary_key=True)
    subtopic_id = Column(Integer, ForeignKey("subtopics.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    difficulty = Column(Integer)  # 1-5
    specialization = Column(String)
    learning_objectives = Column(JSONEncodedDict)
    context_materials = Column(JSONEncodedDict)
    checkpoints = Column(JSONEncodedDict)
    source_url = Column(String)
    source_type = Column(String)  # SCRAPED or GENERATED
    last_updated = Column(DateTime, default=datetime.utcnow)
    share_slug = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    subtopic = relationship("Subtopic", back_populates="case_studies")
    sessions = relationship("Session", back_populates="case_study")

class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(Integer, primary_key=True)
    case_study_id = Column(Integer, ForeignKey("case_studies.id"), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    completed_checkpoints = Column(JSONEncodedDict)
    status = Column(String)
    device_id = Column(String, nullable=False)
    
    case_study = relationship("CaseStudy", back_populates="sessions")
    chat_messages = relationship("ChatMessage", back_populates="session")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    role = Column(String, nullable=False)  # 'user' or 'assistant'
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    checkpoint_id = Column(String)
    
    session = relationship("Session", back_populates="chat_messages")
