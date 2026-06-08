from pydantic import BaseModel

class Product(BaseModel):
    name:str
    price:float
    quantity:int


class UpdateProduct(BaseModel):
    name:str
    price:float
    quantity: int

class SellRequest(BaseModel):
    quantity:  int
    product_id:int