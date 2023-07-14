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


def delete_client(id: int):
    client = session.query(Cliente_entity).get(id)
    if  client is None:
        raise Exception(f" client {id=} not does exist")
    session.delete(client)
    session.commit()

def update_client(id: int, client: Client):
    result = session.query(Cliente_entity).filter(Cliente_entity.id == id).update({Cliente_entity.nombre: client.name,
                                                                                   Cliente_entity.apellido1: client.last_name,
                                                                                   Cliente_entity.apellido2: client.sure_name,
                                                                                   Cliente_entity.numero_identificacion: client.num_id,
                                                                                   Cliente_entity.direccion: client.addres,
                                                                                   Cliente_entity.telefono: client.tel,
                                                                                   Cliente_entity.correo_electronico: client.email},
                                                                                    synchronize_session=False)
    if result == 0:
        raise Exception(f"client {id=} not found")
    if len(client.name.strip())< 1:
        raise Exception("name can not be emptyd")
    if len(client.last_name.strip())< 1:
        raise Exception("last_name can not be emptyd")
    if len(client.sure_name.strip())< 1:
        raise Exception("sure_name can not be emptyd")
    if client.num_id < 1:
        raise Exception("num_id is mandatory")
    if len(client.addres.strip())< 1:
        raise Exception("addres can not be emptyd")
    if client.tel < 1:
        raise Exception("tel is mandatory")
    if len(client.email.strip())< 1:
        raise Exception("email can not be emptyd")
    session.commit()
    return to_client(session.query(Cliente_entity).get(id))


def to_client(client: Cliente_entity):
    return Client(id=client.id,
                  name=client.nombre,
                  last_name=client.apellido1,
                  sure_name=client.apellido2,
                  num_id=client.numero_identificacion,
                  addres=client.direccion,
                  tel=client.telefono,
                  email=client.correo_electronico)