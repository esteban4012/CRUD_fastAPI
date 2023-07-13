from db import session
from models.article import Article, Article_entity


def to_articulo_entity(articulo: Article):
    return Article_entity(id=articulo.id, 
                            list_price=articulo.price, 
                            description=articulo.description, 
                            category_id=articulo.id_category)


def fech_article():
    entities = session.query(Article_entity)
    models = []
    for entity in entities:
        models.append(entity)
    return models