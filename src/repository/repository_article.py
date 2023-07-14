from db import session
from models.article import Article, Article_entity


def to_article_entity(article: Article):
    return Article_entity(id=article.id, 
                            list_price=article.price, 
                            description=article.description, 
                            category_id=article.id_category)


def fech_article():
    entities = session.query(Article_entity)
    models = []
    for entity in entities:
        models.append(entity)
    return models

def add_article(article: Article_entity):
    session.add(article)
    session.commit()

def delete_article(id: int):
    article = session.query(Article_entity).get(id)
    if  article is None:
        raise Exception(f" article {id=} not does exist")
    session.delete(article)
    session.commit()

def update_article(id: int, article: Article):
    result = session.query(Article_entity).filter(Article_entity.id == id).update({Article_entity.list_price: article.price,
                                                                                   Article_entity.description: article.description,
                                                                                   Article_entity.category_id: article.id_category})
    if result == 0:
        raise Exception(f"article {id=} not found")
    
    if article.price < 1:
        raise Exception("price is mandatory")
    if len(article.description.strip()) < 1:
        raise Exception("description can not be emptyd")
    if article.id_category < 1:
        raise Exception("id_category is mandatory")
    
    session.commit()

    return to_article(session.query(Article_entity).get(id))

def to_article(article: Article_entity):
    return Article(id=article.id,
                   description=article.description,
                   price=article.list_price,
                   id_category=article.category_id)

