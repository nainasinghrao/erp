from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

products=[]
@app.get("/")
def home():
    return {"Message": "ERP running"}

class Product(BaseModel):
    id:int
    name:str
    price:float
    quantity:int

@app.post("/products")
def add_prod(product: Product):
    for p in products:
        if p.id==product.id:
            return {"error": "product already exists"}
        
    products.append(product)

    return {
        "message": "product added!",
        "product": product
    }

@app.get("/products")
def view_products():
    return products

@app.get("/products/{product_id}")
def search_prod(product_id:int):

    for product in products:
        if product.id==product_id:
            return product
    return{ "error": "Product not ofund"}


class SellRequest(BaseModel):
    quantity:int

@app.put("/products/{product_id}/sell")
def sell_product(product_id:int, sale:SellRequest):
    for product in products:
        if product.id ==product_id:
            if sale.quantity<=0:
                return {
                    "Error": "sale quantity must be greate thanzero"
                }
            
            if sale.quantity> product.quantity:
                return{"error":"insufficient stock"}
            
            product.quantity-=sale.quantity

            return {
                "messagae": "prodcut sold",
                "remaining product quantity":  product.quantity
            }
        
    return {"error": "product not found"}