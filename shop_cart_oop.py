

class ShoppingCart():
    def __init__(self):
        self.products = []

    def add_product(self):
        type = input("Enter type of product: ").lower()
        quantity = input("Enter the amount you would like: ").lower()
        price = input("Enter the cost of the product you want: ").lower()

        added_product = Product(type,quantity,price)
        self.products.append(added_product)

    def delete_product(self):
        delete_products = input("Enter the product type to remove: ").lower()
        
        for i in range(len(self.products)):
            if self.products[i].type.lower() == delete_products:
                qty_change = input(f"How many {self.products[i].type} do you want now: ").lower()
                self.products[i].quantity = qty_change
                if int(self.products[i].quantity) < 1:
                    print(f"{self.products[i].type} is no longer in cart.")
                    self.products.pop(i)
                    return
                
    
    def print_products(self):
        for inventory in self.products:
            print(f"Item(s): {inventory.type}")
            print(f"Quantity: {inventory.quantity}")
            print(f"Price: ${inventory.price}")

    def run(self):
        while True:
            user_process = input("what can we do for you?(add/remove/show/quit): ")
            
            if user_process == "add":
                self.add_product()
            elif user_process == "remove":
                self.delete_product()
            elif user_process == "show":
                self.print_products()
            elif user_process == 'quit':
                self.print_products()
                return
            else:
                print("Error unable to compute. Please try again")



class Product():
    def __init__(self,type,quantity,price):
        self.type = type
        self.quantity = quantity
        self.price = price

spend = ShoppingCart()
spend.run()

