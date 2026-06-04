class ProductsRepository:
    def __init__(self):
        self.products=[]#now only ProductsRepository can touch products

    def add_product(self,product):
        self.products.append(product)

    def get_products(self):
        return self.products
        
    def get_product(self,product_id):

        for product in self.products:
            if product.id==product_id:
                return product
        return None
        
    def update_product(self,product_id,updated_product):
        product=self.get_product(product_id)
        if product:
            product.name = updated_product.name
            product.price=updated_product.price
            product.quantity=updated_product.quantity

            return product
        
        return None
    

    def delete_product(self, product_id):
        product =self.get_product(product_id)

        if product:
            self.products.remove(product)

            return True
        
        return False

