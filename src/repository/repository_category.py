
from db import session
from models.category import Category, Category_entity


def to_category_entity(category: Category):
    return Category_entity(id=category.id, description=category.description)


def fech_category():
    entities = session.query(Category_entity)
    models = []
    for entity in entities:
        models.append(entity)
    return models

def add_category(category: Category_entity):
    session.add(category)
    session.commit()

def delete_category(id: int):
    category = session.query(Category_entity).get(id)
    if  category is None:
        raise Exception(f" category {id=} not does exist")
    session.delete(category)
    session.commit()

def update_category(id: int, category: Category):
    result = session.query(Category_entity).filter(Category_entity.id == id).update({Category_entity.description: category.description}, synchronize_session=False)
    
    if result == 0:
        raise Exception(f"category {id=} not found")
    if len(category.description.strip()) < 1:
        raise Exception("description can not be empty")
    session.commit()
    
    return to_category(session.query(Category_entity).get(id))

    
def to_category(category: Category_entity):
    return Category(id=category.id, description=category.description)