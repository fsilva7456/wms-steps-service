from pydantic import BaseModel
from typing import Optional

class StepBase(BaseModel):
    step_name: str

class StepCreate(StepBase):
    pass

class Step(StepBase):
    id: int
    
    class Config:
        orm_mode = True