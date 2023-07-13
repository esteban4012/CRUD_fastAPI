from fastapi import FastAPI
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