from sqlalchemy import text
from app.database.connection_db import engine


class ProductsRepository:

    def add_product(self,product):
        with engine.begin() as con:
            con.execute( 
                text(""" INSERT INTO products(name,price,stock)
                     VALUES (:name, :price,:stock)"""
                     ),
                     {
                         "name": product.name,
                         "price": product.price,
                         "stock": product.quantity
                     }
            )

    def get_products(self):
        with engine.begin() as con:
            result= con.execute(
                text("""
                     SELECT *
                     FROM products
                     WHERE is_deleted = FALSE;
                    """)
            )
            return result.mappings().all()
        
    def get_product(self,product_id):

        with engine.begin() as con:
            result = con.execute(
                text("""
                    SELECT *
                    FROM products
                    WHERE id= :id
                    AND is_deleted = FALSE
                """),
                {
                    "id": product_id
                }

            )     
            return result.mappings().first()
            
        
    def update_product(self,product_id,updated_product):
        with engine.begin() as con:
            result= con.execute(
                text("""
                    UPDATE products
                    SET name= :name,
                    price= :price,
                    stock=:stock
                    WHERE id =:id
                     AND is_deleted = FALSE
                    """),
                    {
                        "id":product_id,
                        "name":updated_product.name,
                        "price": updated_product.price,
                        "stock": updated_product.quantity
                    }
            )
            return result.rowcount>0

    def delete_product(self, product_id):
        with engine.begin() as con:
            result = con.execute(
                text("""
                    UPDATE products
                    SET is_deleted=TRUE
                    WHERE id = :id
                """),
                {
                    "id": product_id
                }
            )
            return result.rowcount > 0
        
    def sell_product(self, product_id,quantity):
        with engine.begin() as con:
            con.execute(
                text("""
                    UPDATE products
                     SET stock=stock- :quantity
                     WHERE id=:id
                """),
                {
                    "id": product_id,
                    "quantity":quantity
                }
            )

            con.execute(
                text("""
                    INSERT INTO sales(product_id, quantity_sold)
                     VALUES(:product_id, :quantity)

                """),
                {
                    "product_id": product_id,
                    "quantity": quantity
                }
            )

