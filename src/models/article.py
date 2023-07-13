from pydantic import BaseModel


class Article(BaseModel):
    id : int
    description : str
    price : float
    id_category : int
