from app.repositories.product_repository import ProductsRepository

class ProductsService:
    def __init__(self):
        self.repository= ProductsRepository()

    def add_product_service(self,product):
        
        if product.price<=0:
            return{"error":"Price must be greater than zero"}
        
        if product.quantity <0:
            return {
                "error":"quantity cannot be negative"
            }
        
        self.repository.add_product(product)

        return {"message":"Product added successfully"}
    
    def view_products_service(self):
        return self.repository.get_products()
    
    def search_product_service(self,product_id):
        product= self.repository.get_product(product_id)
    
        if product is None:
            return {
                "error":"Product not found"
            }
        
        return product
    
    def sell_product_service(self, request):
        product= self.repository.get_product(request.product_id)

        if product is None:
            return { "error":"Product not found"}
        
        if request.quantity<=0:
            return {
                "error":"Quantity must be greater than zero"
            }

        if request.quantity>product["stock"]:
            return {"error": "Insufficient stock"}
        
        self.repository.sell_product(request.product_id,request.quantity)

        return{
            "message":"product sold",
            "remaining_stock": product["stock"]-request.quantity
        }
    
    def update_product_service(self,product_id,updated_product):
        updated= self.repository.update_product(product_id, updated_product)
        if not updated:
            return {"error":"product not found"}

        return {"message": "product updates successfully"}
    
    def delete_product_service(self,product_id):
        deleted=self.repository.delete_product(product_id)

        if not deleted:
            return {"error":"product not found"}
        
        return {"message":"product delted"}


