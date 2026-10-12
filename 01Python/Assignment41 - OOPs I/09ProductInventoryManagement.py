'''
Assignment 9: Product Inventory Management

A shopkeeper wants to manage the stock of a product.

Create a class Product with the following attributes:
- Product ID
- Product name
- Price
- Available quantity

Create the following methods:
- add_stock() – Increase the available quantity.
- sell_product() – Decrease the available quantity.
- calculate_stock_value() – Calculate price × available quantity.
- display_product() – Display product and stock details.

Sample operations:

Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3

Expected result:

Available Quantity: 12
Total Stock Value: 540000
'''
class Product:

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity=self.quantity+amount
        return self.quantity
    def sell_product(self, amount):
        self.quantity=self.quantity-amount
        return self.quantity
        

    def calculate_stock_value(self):
        return self.price*self.quantity

    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Available Quantity: {self.quantity}")
        print(f"Total Stock Value: {self.calculate_stock_value()}")

p1 = Product(101, "Laptop", 45000, 10)

p1.add_stock(5)
p1.sell_product(3)

p1.display_product()