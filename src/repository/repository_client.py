from db import session
from models.client import Client, Cliente_entity


def to_client_entity(cliente: Client):
    return Cliente_entity(id= cliente.id,
                          nombre=cliente.name, 
                          apellido1=cliente.last_name, 
                          apellido2=cliente.sure_name, 
                          numero_identificacion=cliente.num_id, 
                          direccion=cliente.addres, 
                          telefono=cliente.tel, 
                          correo_electronico=cliente.email)



def fech_clients():
    entities = session.query(Cliente_entity)
    models = []
    for entity in entities:
        models.append(entity)
    return models


def add_client(client: Cliente_entity):
    session.add(client)
    session.commit()