products={}
def add_prod():
    product_id=input("Enter product ID: ")
    if product_id in products:
        print("Product already exists")
        return
    
    name=input("Enter product name: ")
    if not name:
        print("Product namecannot be empty")
        return
    
    try:
        price=float(input("Enter product price: "))
        if price<=0:
            print("Price cannot benegative")
            return
        
        quantity=int(input("enter product quantityy: "))
        if quantity<0:
            print("quantity cannot be negative")
            return
        
    except ValueError:
        print("Invalid input")
        return
    
    products[product_id]={
        "name":name,
        "price": price,
        "quantity":quantity
    }

    print("product added")

def view_prods():
    print("Product list: \n")
    if not products:
        print("No products present")
        return
    
    for product_id, details in products.items():
        print(f"Product ID: {product_id}")
        print(f"Product name: {details['name']}")
        print(f"Product price: {details['price']}")
        print(f"Product quantity: {details["quantity"]}")

def search_prod():
    key=input("Enter product ID").lower()

    found = False
    for product_id,details in products.items():
        if(key==product_id.lower()):
            print(f"Product ID: {product_id}")
            print(f"Product name: {details['name']}")
            print(f"Product price: {details['price']}")
            print(f"Product quantity: {details["quantity"]}")
            
            found=True

        else:
            print("Product not found")


def sell_prod():
    product_id=input("Enter product ID:")
    if product_id not in  products:
        print("Product not found")
        return
    
    try:
        sell_quantity=int(input("Enter the quantity to sell: "))
        if sell_quantity<=0:
            print("Quantity must be greater than 0")
            return
        
    except ValueError:
        print("Invalid quantity")
        return
    
    available_qty=products[product_id]["quantity"]

    if sell_quantity> available_qty:
        print("Insufficient stock")
        return
    
    products[product_id]["quantity"] -= sell_quantity

    total= sell_quantity * products[product_id]["price"]
    print(f"Total Amount: {total}")

    print("Sale successful")

    if products[product_id]["quantity"]==0:
        print("Out of stock")

def main():
    while True:
        print("ERP")
        print("1. Add product")
        print("2. View product")
        print("3. Search product")
        print("4. Sell product")
        print("5.Exit")

        choice= input("Enter choice")
        if choice == "1":
            add_prod()
            
        elif choice == "2":
            view_prods()

        elif choice == "3":
            search_prod()

        elif choice == "4":
            sell_prod()

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if  __name__=="__main__":
    main()