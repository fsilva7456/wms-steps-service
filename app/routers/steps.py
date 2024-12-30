from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/steps", tags=["Steps"])

@router.get("/", response_model=list[schemas.Step])
def get_all_steps(db: Session = Depends(get_db)):
    return db.query(models.Step).all()

@router.post("/", response_model=schemas.Step)
def create_step(step_data: schemas.StepCreate, db: Session = Depends(get_db)):
    step = models.Step(step_name=step_data.step_name)
    db.add(step)
    db.commit()
    db.refresh(step)
    return step