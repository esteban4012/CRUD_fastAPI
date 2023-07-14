from models.orders import Orders, Orders_entity
from db import session

def to_orders_entity(orden: Orders):
   
    return Orders_entity(id=orden.id,
                          fecha=orden.date, 
                          id_cliente=orden.id_client)

def fech_orders():
    entities = session.query(Orders_entity)
    models = []
    for entity in entities:
        models.append(entity)
    return models