from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/{step_id}", response_model=schemas.Step)
def get_step(step_id: int, db: Session = Depends(get_db)):
    step = db.query(models.Step).filter(models.Step.id == step_id).first()
    if not step:
        raise HTTPException(status_code=404, detail="Step not found")
    return step

@router.put("/{step_id}", response_model=schemas.Step)
def update_step(step_id: int, step_data: schemas.StepCreate, db: Session = Depends(get_db)):
    step = db.query(models.Step).filter(models.Step.id == step_id).first()
    if not step:
        raise HTTPException(status_code=404, detail="Step not found")
    step.step_name = step_data.step_name
    db.commit()
    db.refresh(step)
    return step