from fastapi import FastAPI, HTTPException
from models.client import Client


app = FastAPI()

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
        return HTTPException(status_code=404, detail="name can not be emptyd")
    if len(client.sure_name.strip()) < 1:
        return HTTPException(status_code=404, detail="name can not be emptyd")
    if client.num_id < 1:
        return HTTPException(status_code=404, detail="id_mum is mandatory")
    if len(client.addres.strip()) < 1:
        return HTTPException(status_code=404, detail="name can not be emptyd")
    if client.tel < 1:  
        return HTTPException(status_code=404, detail="tel is mandatory")
    if len(client.email.strip()) < 1:
        return HTTPException(status_code=404, detail="name can not be emptyd")
    
    edit.name = client.name
    edit.last_name = client.last_name
    edit.sure_name = client.sure_name
    edit.num_id = client.num_id
    edit.addres = client.addres
    edit.tel = client.tel
    edit.email = client.email
    return edit
