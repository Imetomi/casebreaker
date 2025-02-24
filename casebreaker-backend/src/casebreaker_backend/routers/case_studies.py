from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
import uuid
from datetime import datetime

from ..database import get_db
from ..models import CaseStudy as CaseStudyModel, Subtopic as SubtopicModel
from ..schemas import CaseStudy, CaseStudyCreate

router = APIRouter(prefix="/case-studies", tags=["case_studies"])


def generate_share_slug() -> str:
    """Generate a unique 8-character slug for sharing."""
    return str(uuid.uuid4())[:8]


def get_case_count(db: Session, subtopic_id: int) -> int:
    """Get the number of case studies for a given subtopic."""
    return (
        db.query(func.count(CaseStudyModel.id))
        .filter(CaseStudyModel.subtopic_id == subtopic_id)
        .scalar()
    )


def get_case_study_by_id_or_404(db: Session, case_study_id: int) -> CaseStudyModel:
    """Get a case study by ID or raise 404 if not found."""
    case_study = (
        db.query(CaseStudyModel).filter(CaseStudyModel.id == case_study_id).first()
    )
    if case_study is None:
        raise HTTPException(status_code=404, detail="Case study not found")
    return case_study


def get_subtopic_by_id_or_404(db: Session, subtopic_id: int) -> SubtopicModel:
    """Get a subtopic by ID or raise 404 if not found."""
    subtopic = db.query(SubtopicModel).filter(SubtopicModel.id == subtopic_id).first()
    if not subtopic:
        raise HTTPException(status_code=404, detail="Subtopic not found")
    return subtopic


@router.post("/", response_model=CaseStudy)
def create_case_study(case_study: CaseStudyCreate, db: Session = Depends(get_db)):
    """Create a new case study."""
    # Verify subtopic exists
    subtopic = get_subtopic_by_id_or_404(db, case_study.subtopic_id)

    # Create the case study
    db_case_study = CaseStudyModel(
        **case_study.model_dump(),
        share_slug=generate_share_slug(),
        last_updated=datetime.utcnow(),
        created_at=datetime.utcnow()
    )
    db.add(db_case_study)
    db.commit()
    db.refresh(db_case_study)

    # Set the case count
    db_case_study.subtopic.case_count = get_case_count(db, case_study.subtopic_id)

    return {
        "id": db_case_study.id,
        "title": db_case_study.title,
        "description": db_case_study.description,
        "difficulty": db_case_study.difficulty,
        "specialization": db_case_study.specialization,
        "learningObjectives": db_case_study.learning_objectives,
        "contextMaterials": db_case_study.context_materials,
        "checkpoints": db_case_study.checkpoints,
        "pitfalls": db_case_study.pitfalls,
        "sourceUrl": db_case_study.source_url,
        "sourceType": db_case_study.source_type,
        "lastUpdated": db_case_study.last_updated,
        "shareSlug": db_case_study.share_slug,
        "createdAt": db_case_study.created_at,
        "estimatedTime": db_case_study.estimated_time,
    }


@router.get("/", response_model=List[CaseStudy])
def list_case_studies(subtopic_id: Optional[int] = None, db: Session = Depends(get_db)):
    """List all case studies, optionally filtered by subtopic_id."""
    # Build the query
    query = db.query(CaseStudyModel)
    if subtopic_id:
        query = query.filter(CaseStudyModel.subtopic_id == subtopic_id)

    # Get all case studies
    case_studies = query.all()

    # Get unique subtopic IDs from the results
    subtopic_ids = {case.subtopic_id for case in case_studies}

    # Get case counts for each subtopic
    subtopic_counts = {}
    for subtopic_id in subtopic_ids:
        subtopic_counts[subtopic_id] = get_case_count(db, subtopic_id)

    # Update each case study's subtopic with its count
    for case in case_studies:
        case.subtopic.case_count = subtopic_counts[case.subtopic_id]

    return case_studies


@router.get("/{case_study_id}", response_model=CaseStudy)
def get_case_study(case_study_id: int, db: Session = Depends(get_db)):
    """Get a case study by its ID."""
    db_case_study = get_case_study_by_id_or_404(db, case_study_id)
    db_case_study.subtopic.case_count = get_case_count(db, db_case_study.subtopic_id)
    return db_case_study


@router.get("/by-slug/{share_slug}", response_model=CaseStudy)
def get_case_study_by_slug(share_slug: str, db: Session = Depends(get_db)):
    """Get a case study by its share slug."""
    db_case_study = (
        db.query(CaseStudyModel).filter(CaseStudyModel.share_slug == share_slug).first()
    )
    if db_case_study is None:
        raise HTTPException(status_code=404, detail="Case study not found")

    db_case_study.subtopic.case_count = get_case_count(db, db_case_study.subtopic_id)
    return db_case_study


@router.delete("/{case_study_id}")
def delete_case_study(case_study_id: int, db: Session = Depends(get_db)):
    """Delete a case study by its ID."""
    db_case_study = get_case_study_by_id_or_404(db, case_study_id)
    db.delete(db_case_study)
    db.commit()
    return {"message": "Case study deleted"}
