from fastapi import APIRouter
from app.controllers.product_controller import ProductController
from app.models.product_model import Product,UpdateProduct,SellRequest

router = APIRouter()
controller = ProductController()

@router.post("/products")
def add_product(product: Product):
    return controller.add_product_controller(product)

@router.get("/products")
def view_products():
    return controller.view_products_controller()

@router.get("/products/{product_id}")
def search_product(product_id: int):
    return controller.search_product_controller(product_id)

@router.put("/products/sell")
def sell_product(request: SellRequest):
    return controller.sell_product_controller(request)

@router.put("/products/{product_id}")
def update_product(product_id: int,updated_product: UpdateProduct):
    return controller.update_product_controller(product_id,updated_product)

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    return controller.delete_product_controller(product_id)