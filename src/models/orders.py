from pydantic import BaseModel


class Orders(BaseModel):
    id : int
    date : str
    id_client : int