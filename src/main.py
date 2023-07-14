from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models.client import Client
from models.orders import Orders, Orders_entity
from models.article import Article
from models.category import Category
import repository.repository_client
from repository.repository_category import to_category_entity
import repository.repository_category
import repository.repository_article
import repository.repository_order
from repository.repository_order import to_orders_entity
app = FastAPI()


# CRUD CLIENT

data_clients = {
    "client" : {
        1 : Client(id=1,name = "esteban", last_name = "agudelo" , sure_name = "hurtado", num_id= 1813644740, addres= "calle 65a" , tel= 3160100915 , email= "esteban@gamil.com"),
        
    }   
}


@app.get("/clients", tags=['clients'])
async def read_clients():
    return repository.repository_client.fech_clients()


@app.post("/clients", tags=['clients'])
async def create_client(client: Client):
    clients = data_clients["client"]
    clients[client.id] = client
    return data_clients["client"]


@app.put("/clients/{id}", tags=["clients"])
async def edit_clients(id : int, client: Client):
    clients = data_clients["client"]
    if  id not in clients:
        return HTTPException(status_code=404, detail=f"client with {id=} does not exist")

    edit = clients[id]
    if len(client.name.strip()) < 1:
        return HTTPException(status_code=404, detail=" name can not be emptyd")
    if len(client.last_name.strip()) < 1:
        return HTTPException(status_code=404, detail="last_name can not be emptyd")
    if len(client.sure_name.strip()) < 1:
        return HTTPException(status_code=404, detail="sure_name can not be emptyd")
    if client.num_id < 1:
        return HTTPException(status_code=404, detail="num_id is mandatory")
    if len(client.addres.strip()) < 1:
        return HTTPException(status_code=404, detail="addres can not be emptyd")
    if client.tel < 1:  
        return HTTPException(status_code=404, detail="tel is mandatory")
    if len(client.email.strip()) < 1:
        return HTTPException(status_code=404, detail="email can not be emptyd")
    
    edit.name = client.name
    edit.last_name = client.last_name
    edit.sure_name = client.sure_name
    edit.num_id = client.num_id
    edit.addres = client.addres
    edit.tel = client.tel
    edit.email = client.email
    return edit


@app.delete("/clients/{id}", tags=['clients'])
async def delete_client(id: int):
    client = data_clients["client"]
    if id not in client:
        return HTTPException(status_code=404 , detail= f"client with {id=}, does not exist")
    client.pop(id)
    return data_clients 


# CRUD ORDERS

data_orders = {
    "orders" : {
        1 : Orders(id = 1 ,date= "2023-07-12", id_client = 1 )
    }
}

@app.get("/orders", tags=["orders"])
async def read_orders():
    return repository.repository_order.fech_orders()


@app.post("/orders", tags=["orders"])
async def create_orders(order : Orders):
    repository.repository_order.add_order(to_orders_entity(order))
    return JSONResponse(status_code=200,content="order create")


@app.put("/orders/{id}", tags=["orders"])
async def edit_orders(id : int , ordens : Orders):
    order = data_orders["orders"]
    if id not in order:
        return HTTPException(status_code=404,detail=f"order with {id=}, does not exist")
    
    edit = order[id]
    if ordens.id < 1:
        return HTTPException(status_code=404, detail="id is mandatory")
    
    if len(ordens.date.strip()) < 1:
        return HTTPException(status_code=404, detail="date can not be emptyd")
    
    if ordens.id_client < 1:
        return HTTPException(status_code=404, detail="id_client is mandatory")
    
    edit.date = ordens.date
    edit.id_client = ordens.id_client
    return edit
    

@app.delete("/orders/{id}", tags=["orders"])
async def delete_order(id: int):
    order = data_orders["orders"]
    if id not in order:
        return HTTPException(status_code=404,detail=f"client with {id=}, does not exist")
    order.pop(id)
    return data_orders


# CRUD ARTICLE


data_article = {
    "article" : {
        1 : Article(id=1,description="comedor",price=1000000,id_category=1)
    }
}

@app.get("/article", tags=["article"])
async def read_article():
    return repository.repository_article.fech_article()


@app.post("/article", tags=["article"])
async def create_article(articles : Article):
    article = data_article["article"]
    article[articles.id] = articles
    return data_article


@app.put("/article/{id}", tags=["article"])
async def edit_article(id : int , article : Article):
    articles = data_article["article"]
    if id not in articles:
        return HTTPException(status_code=404,detail=f"orden with {id=}, does not exist")
    
    if  article.id < 1:
        return HTTPException(status_code=404, detail="id is mandatory")
    if len(article.description.strip()) < 1:
        return HTTPException(status_code=404, detail="description can not be emptyd")
    if article.price < 1:
        return HTTPException(status_code=404, detail="price is mandatory")
    if article.id_category < 1:
        return HTTPException(status_code=404, detail="id_category is mandatory")
    
    edit = articles[id]
    
    edit.description = article.description
    edit.price = article.price
    edit.id_category = article.id_category
    return edit


@app.delete("/article/{id}", tags=["article"])
async def delete_article(id: int):
    articles = data_article["article"]
    if id not in articles:
        return HTTPException(status_code=404,detail=f"orden with {id=}, does not exist")
    
    articles.pop(id)
    return data_article


# CRUD CATEGORY

data_category = {
    "category" : {
        1 : Category(id=1, description="salas")
}}


@app.get("/category", tags=["category"])
async def read_category():
    return repository.repository_category.fech_category()


@app.post("/category", tags=["category"])
async def create_category(category : Category):
    repository.repository_category.add_category(to_category_entity(category))
    return JSONResponse(status_code=200, content= "category create")


@app.put("/category/{id}", tags=["category"])
async def edit_category(id : int, category: Category):
    categorys = data_category["category"]
    if id not in categorys:
        return HTTPException(status_code=404,detail=f"category with {id=}, does not exist")
    
    if category.id < 1:
        return HTTPException(status_code=404, detail="id is mandatory")
    
    if len(category.description.strip()) < 1:
        return HTTPException(status_code=404, detail="description can not be empty")
    
    edit = categorys[id]
    edit.description = category.description
    return edit


@app.delete("/category/{id}", tags=["category"])
async def delete_category(id : int):
    categorys = data_category["category"]
    if id not in categorys:
        return HTTPException(status_code=404,detail=f"orden with {id=}, does not exist")
    categorys.pop(id)
    return data_category
