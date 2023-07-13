from fastapi import FastAPI, HTTPException
from models.client import Client
from models.orders import Orders
from models.article import Article


app = FastAPI()


# CRUD CLIENT

data_clients = {
    "client" : {
        1 : Client(id=1,name = "esteban", last_name = "agudelo" , sure_name = "hurtado", num_id= 1813644740, addres= "calle 65a" , tel= 3160100915 , email= "esteban@gamil.com"),
        
    }   
}


@app.get("/clients", tags=['clients'])
async def read_clients():
    return data_clients


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
    return data_orders["orders"]


@app.post("/orders", tags=["orders"])
async def create_orders(orderns : Orders):
    order = data_orders["orders"]
    order[orderns.id] = orderns
    return data_orders 


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
    "articulo" : {
        1 : Article(id=1,description="comedor",price=1000000,id_category=1)
    }
}

@app.get("/article", tags=["article"])
async def read_article():
    return data_article

