
from models.category import Category_entity
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DECIMAL,Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from typing import Optional
import db


class Article(BaseModel):
    id : Optional[int] = None
    description : str
    price : float
    id_category : int

class Articulos_entity(db.Base):

    __tablename__ = "items"

    id = Column(Integer,primary_key=True)
    list_price = Column(DECIMAL(10,2))
    description = Column(String(100))
    category_id: int = Column(ForeignKey("category.id"))
    category : Mapped["Category_entity"] = relationship()
    
    def __init__(self, id, list_price, description, category_id):

        self.id = id
        self.list_price = list_price
        self.description = description
        self.category_id = category_id

    def __repr__(self):
        return f"articulos({self.id}, {self.list_price}, {self.description}, {self.category_id})"
