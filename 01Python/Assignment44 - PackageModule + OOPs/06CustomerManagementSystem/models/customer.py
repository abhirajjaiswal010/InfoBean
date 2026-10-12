class Customer:

    def __init__(self, customer_id, customer_name, city, purchase_amount):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.city = city
        self.purchase_amount = purchase_amount

    def display(self):
        print(f"{self.customer_id} {self.customer_name} {self.city} {self.purchase_amount}")

    def search(self, id):
        return self.customer_id == id

    def city_customer(self, city):
        return self.city == city

    def purchase_greater_10000(self):
        return self.purchase_amount > 10000

    def highest(self, other):
        return self.purchase_amount > other.purchase_amount

    def total_sales(self, customers):
        total = 0

        for c in customers:
            total += c.purchase_amount

        return total

    def average_purchase(self, customers):
        total = self.total_sales(customers)

        return total / len(customers)