from pydantic import BaseModel

class Client(BaseModel):
    id : int
    name : str
    last_name : str
    sure_name : str
    num_id : int
    addres : str
    tel : int
    email : str

