from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid
from datetime import datetime

from ..database import get_db
from ..models import CaseStudy as CaseStudyModel, Subtopic as SubtopicModel
from ..schemas import CaseStudy, CaseStudyCreate

router = APIRouter(prefix="/case-studies", tags=["case_studies"])


def generate_share_slug():
    return str(uuid.uuid4())[:8]


@router.post("/", response_model=CaseStudy)
def create_case_study(case_study: CaseStudyCreate, db: Session = Depends(get_db)):
    # Verify subtopic exists
    subtopic = (
        db.query(SubtopicModel)
        .filter(SubtopicModel.id == case_study.subtopic_id)
        .first()
    )
    if not subtopic:
        raise HTTPException(status_code=404, detail="Subtopic not found")

    db_case_study = CaseStudyModel(
        **case_study.model_dump(),
        share_slug=generate_share_slug(),
        last_updated=datetime.utcnow(),
        created_at=datetime.utcnow()
    )
    db.add(db_case_study)
    db.commit()
    db.refresh(db_case_study)
    return db_case_study


@router.get("/", response_model=List[CaseStudy])
def list_case_studies(subtopic_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(CaseStudyModel)
    if subtopic_id:
        query = query.filter(CaseStudyModel.subtopic_id == subtopic_id)
    return query.all()


@router.get("/{case_study_id}", response_model=CaseStudy)
def get_case_study(case_study_id: int, db: Session = Depends(get_db)):
    db_case_study = (
        db.query(CaseStudyModel).filter(CaseStudyModel.id == case_study_id).first()
    )
    if db_case_study is None:
        raise HTTPException(status_code=404, detail="Case study not found")
    return db_case_study


@router.get("/by-slug/{share_slug}", response_model=CaseStudy)
def get_case_study_by_slug(share_slug: str, db: Session = Depends(get_db)):
    db_case_study = (
        db.query(CaseStudyModel).filter(CaseStudyModel.share_slug == share_slug).first()
    )
    if db_case_study is None:
        raise HTTPException(status_code=404, detail="Case study not found")
    return db_case_study


@router.delete("/{case_study_id}")
def delete_case_study(case_study_id: int, db: Session = Depends(get_db)):
    db_case_study = (
        db.query(CaseStudyModel).filter(CaseStudyModel.id == case_study_id).first()
    )
    if db_case_study is None:
        raise HTTPException(status_code=404, detail="Case study not found")
    db.delete(db_case_study)
    db.commit()
    return {"message": "Case study deleted"}
