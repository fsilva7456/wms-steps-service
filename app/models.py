from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Step(Base):
    __tablename__ = "steps"
    
    id = Column(Integer, primary_key=True, index=True)
    step_name = Column(String(255), nullable=False)