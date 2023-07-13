from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, DECIMAL
import db


class Client(BaseModel):
    id : Optional[int] = None
    name : str
    last_name : str
    sure_name : str
    num_id : int
    addres : str
    tel : int
    email : str

class Cliente_entity(db.Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido1 = Column(String(50), nullable=False)
    apellido2 = Column(String(50),nullable=True)
    numero_identificacion = Column(DECIMAL(15,0),nullable=False)
    direccion = Column(String(50),nullable=False)
    telefono = Column(DECIMAL(15,0),nullable=False)
    correo_electronico = Column(String(50),nullable=False)
   



    def __init__(self,id ,nombre, apellido1, apellido2, numero_identificacion, direccion, telefono, correo_electronico):
        self.id = id
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.numero_identificacion = numero_identificacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    def __repr__(self):
        return f'clientes({self.id},{self.nombre}, {self.apellido1}, {self.apellido2}, {self.numero_identificacion}, {self.direccion}, {self.telefono}, {self.correo_electronico})'


