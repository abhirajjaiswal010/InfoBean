class Product:

    def __init__(self,product_id,product_name,price,quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.quantity=quantity

    def display(self):
        print(f'{self.product_id} {self.product_name} {self.price} {self.quantity}')

    def total_value(self):
        print(f"{self.product_name} = {self.quantity*self.price}")

    def quantity_lessthan10(self):
        return self.quantity<10
    
    def highest(self,other):
        return self.price>other.price
    
    def total_inventory(self,total):
        total+=(self.price*self.quantity)
        return total
    def search(self,id):
        return self.product_id==id


        