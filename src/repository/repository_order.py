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

def add_order(order: Orders_entity):
    session.add(order)
    session.commit()

def delete_order(id: int):
    order = session.query(Orders_entity).get(id)
    if order is None:
        raise Exception(f"order {id=} not does exist")
    session.delete(order)
    session.commit()

def update_order(id: int, order: Orders):
    result = session.query(Orders_entity).filter(Orders_entity.id == id).update({Orders_entity.fecha: order.date,
                                                                                 Orders_entity.id_cliente: order.id_client})
    if result == 0:
        raise Exception(f"order {id=} not found")
    if len(order.date.strip())< 1:
        raise Exception(f"date can not be emptyd")
    if order.id_client < 0:
        raise Exception("id_client is mandatory")
    session.commit()
    
    return to_order(session.query(Orders_entity).get(id))


def to_order(order: Orders_entity):
    return Orders(id=order.id,
                  date=order.fecha.__str__(),
                  id_client= order.id_cliente)
 




