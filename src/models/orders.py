from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from .client import Cliente_entity
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Date
import db


class Orders(BaseModel):
    id : Optional[int] = None
    date : str
    id_client : int


class Orders_entity(db.Base):
    __tablename__ = "ordenes"
    
    
    id = Column(Integer,primary_key=True, nullable=False)
    fecha = Column(Date)
    id_cliente: int = Column(ForeignKey("clientes.id"))
    clientes : Mapped["Cliente_entity"] = relationship() 



    def __init__(self,id, fecha, id_cliente):
        
        self.id = id
        self.fecha = fecha
        self.id_cliente = id_cliente

    def __repr__(self):
        return f"ordenes ({self.id}, {self.fecha}, {self.id_cliente})"