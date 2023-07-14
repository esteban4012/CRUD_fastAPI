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