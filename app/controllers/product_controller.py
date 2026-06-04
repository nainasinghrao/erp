from services.product_service import ProductsService

class ProductController:
    def __init__(self):
        self.service = ProductsService()

    def add_product_controller(self, product):
        return self.service.add_product_service(product)

    def view_products_controller(self):
        return self.service.view_products_service()

    def search_product_controller(self, product_id):
        return self.service.search_product_service(product_id)

    def sell_product_controller(self, request):
        return self.service.sell_product_service(request)

    def update_product_controller(self,product_id,updated_product):
        return self.service.update_product_service(product_id,updated_product)

    def delete_product_controller(self, product_id):
        return self.service.delete_product_service(product_id)