from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Field as FieldModel
from ..schemas import Field, FieldCreate

router = APIRouter(
    prefix="/fields",
    tags=["fields"]
)

@router.post("/", response_model=Field)
def create_field(field: FieldCreate, db: Session = Depends(get_db)):
    db_field = FieldModel(**field.model_dump())
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field

@router.get("/", response_model=List[Field])
def list_fields(db: Session = Depends(get_db)):
    return db.query(FieldModel).all()

@router.get("/{field_id}", response_model=Field)
def get_field(field_id: int, db: Session = Depends(get_db)):
    db_field = db.query(FieldModel).filter(FieldModel.id == field_id).first()
    if db_field is None:
        raise HTTPException(status_code=404, detail="Field not found")
    return db_field

@router.delete("/{field_id}")
def delete_field(field_id: int, db: Session = Depends(get_db)):
    db_field = db.query(FieldModel).filter(FieldModel.id == field_id).first()
    if db_field is None:
        raise HTTPException(status_code=404, detail="Field not found")
    db.delete(db_field)
    db.commit()
    return {"message": "Field deleted"}
