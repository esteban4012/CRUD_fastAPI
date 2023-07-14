from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models.client import Client
from models.orders import Orders
from models.article import Article
from models.category import Category
import repository.repository_client
import repository.repository_category
import repository.repository_article
import repository.repository_order
from repository.repository_order import to_orders_entity
from repository.repository_article import to_article_entity
from repository.repository_client import to_client_entity
from repository.repository_category import to_category_entity
app = FastAPI()


# CRUD CLIENT

@app.get("/clients", tags=['clients'])
async def read_clients():
    return repository.repository_client.fech_clients()


@app.post("/clients", tags=['clients'])
async def create_client(client: Client):
    repository.repository_client.add_client(to_client_entity(client))
    return JSONResponse(status_code=200, content="client create")


@app.put("/clients/{id}", tags=["clients"])
async def edit_clients(id : int, client: Client):
    return repository.repository_client.update_client(id,client)


@app.delete("/clients/{id}", tags=["clients"])
async def delete_client(id : int):
    try:
        repository.repository_client.delete_client(id)
    
    except:
        return HTTPException(status_code=404, detail="it was not possible to delete the client")
    
    return JSONResponse(status_code=200,content="client delete")



# CRUD ORDERS

@app.get("/orders", tags=["orders"])
async def read_orders():
    return repository.repository_order.fech_orders()


@app.post("/orders", tags=["orders"])
async def create_orders(order : Orders):
    repository.repository_order.add_order(to_orders_entity(order))
    return JSONResponse(status_code=200,content="order create")


@app.put("/orders/{id}", tags=["orders"])
async def edit_orders(id : int , ordens : Orders):
    return repository.repository_order.update_order(id,ordens)
    

@app.delete("/orders/{id}", tags=["orders"])
async def delete_order(id: int):
    try:
        repository.repository_order.delete_order(id)
    except:
        return HTTPException(status_code=404, detail="it was not possible to delete the order")
    
    return JSONResponse(status_code=200, content= "order delete")


# CRUD ARTICLE

@app.get("/article", tags=["article"])
async def read_article():
    return repository.repository_article.fech_article()


@app.post("/article", tags=["article"])
async def create_article(article : Article):
    repository.repository_article.add_article(to_article_entity(article))
    return JSONResponse(status_code=200, content= "article create")

@app.put("/article/{id}", tags=["article"])
async def edit_article(id : int , article : Article):
    return repository.repository_article.update_article(id, article)

@app.delete("/article/{id}", tags=["article"])
async def delete_article(id : int):
    try:
        repository.repository_article.delete_article(id)
    
    except:
        return HTTPException(status_code=404, detail="it was not possible to delete the article")
    
    return JSONResponse(status_code=200,content="article delete")


# CRUD CATEGORY

@app.get("/category", tags=["category"])
async def read_category():
    return repository.repository_category.fech_category()


@app.post("/category", tags=["category"])
async def create_category(category : Category):
    repository.repository_category.add_category(to_category_entity(category))
    return JSONResponse(status_code=200, content= "category create")


@app.put("/category/{id}", tags=["category"])
async def edit_category(id : int, category: Category):
    return repository.repository_category.update_category(id,category)
    

@app.delete("/category/{id}", tags=["category"])
async def delete_category(id : int):
    try:
        repository.repository_category.delete_category(id)
    
    except:
        return HTTPException(status_code=404, detail="it was not possible to delete the category")
    
    return JSONResponse(status_code=200,content="category delete")