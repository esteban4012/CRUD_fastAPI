from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column
from typing import Optional
import db


class Category(BaseModel):
    id : Optional[int] = None
    description : str


class Category_entity(db.Base):

    __tablename__ = "category"

    id = Column(Integer,primary_key=True)
    description = Column(String(200), nullable=False)
    

    def __init__(self, id, description ):

        self.id = id
        self.description = description

    def __repr__(self):
        return f"category({self.id}, {self.description})"