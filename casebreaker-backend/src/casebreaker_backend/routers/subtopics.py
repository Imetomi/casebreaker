from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from ..database import get_db
from ..models import Subtopic as SubtopicModel, Field as FieldModel
from ..schemas import Subtopic, SubtopicCreate

router = APIRouter(prefix="/subtopics", tags=["subtopics"])


@router.post("/", response_model=Subtopic)
def create_subtopic(subtopic: SubtopicCreate, db: Session = Depends(get_db)):
    # Verify field exists
    field = db.query(FieldModel).filter(FieldModel.id == subtopic.field_id).first()
    if not field:
        raise HTTPException(status_code=404, detail="Field not found")

    db_subtopic = SubtopicModel(**subtopic.model_dump())
    db.add(db_subtopic)
    db.commit()
    db.refresh(db_subtopic)
    return db_subtopic


@router.get("/", response_model=List[Subtopic])
def list_subtopics(field_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(SubtopicModel).options(joinedload(SubtopicModel.case_studies))
    if field_id:
        query = query.filter(SubtopicModel.field_id == field_id)
    subtopics = query.all()

    # Convert to response model with case count
    response_subtopics = []
    for subtopic in subtopics:
        subtopic_dict = {
            "id": subtopic.id,
            "name": subtopic.name,
            "description": subtopic.description,
            "field_id": subtopic.field_id,
            "field": subtopic.field,
            "case_count": len(subtopic.case_studies),
        }
        response_subtopics.append(subtopic_dict)

    return response_subtopics


@router.get("/{subtopic_id}", response_model=Subtopic)
def get_subtopic(subtopic_id: int, db: Session = Depends(get_db)):
    db_subtopic = (
        db.query(SubtopicModel).filter(SubtopicModel.id == subtopic_id).first()
    )
    if db_subtopic is None:
        raise HTTPException(status_code=404, detail="Subtopic not found")
    return db_subtopic


@router.delete("/{subtopic_id}")
def delete_subtopic(subtopic_id: int, db: Session = Depends(get_db)):
    db_subtopic = (
        db.query(SubtopicModel).filter(SubtopicModel.id == subtopic_id).first()
    )
    if db_subtopic is None:
        raise HTTPException(status_code=404, detail="Subtopic not found")
    db.delete(db_subtopic)
    db.commit()
    return {"message": "Subtopic deleted"}
