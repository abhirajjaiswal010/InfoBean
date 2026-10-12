from models.customer import Customer

print("-" * 20)
print("CUSTOMER MANAGEMENT SYSTEM")
print("-" * 20)

customerDB = []

print("Enter Customer Details")

for i in range(5):

    print("Customer", i + 1)

    customer_id = int(input("Enter Customer ID : "))
    customer_name = input("Enter Customer Name : ")
    city = input("Enter City : ")
    purchase_amount = int(input("Enter Purchase Amount : "))

    customer = Customer(
        customer_id,
        customer_name,
        city,
        purchase_amount
    )

    customerDB.append(customer)

print("-" * 20)
print("ALL CUSTOMERS")
print("-" * 20)

for c in customerDB:
    c.display()

print("-" * 20)
print("CUSTOMERS FROM CITY")
print("-" * 20)

city = input("Enter City : ")

for c in customerDB:
    if c.city_customer(city):
        c.display()

print("-" * 20)
print("PURCHASE GREATER THAN 10000")
print("-" * 20)

for c in customerDB:
    if c.purchase_greater_10000():
        c.display()

print("-" * 20)
print("HIGHEST PURCHASE CUSTOMER")
print("-" * 20)

high = customerDB[0]

for c in customerDB:
    if c.highest(high):
        high = c

high.display()

print("-" * 20)
print("TOTAL SALES")
print("-" * 20)

print(customerDB[0].total_sales(customerDB))

print("-" * 20)
print("AVERAGE PURCHASE AMOUNT")
print("-" * 20)

print(customerDB[0].average_purchase(customerDB))

print("-" * 20)
print("SEARCH CUSTOMER")
print("-" * 20)

customer_id = int(input("Enter Customer ID : "))

for c in customerDB:
    if c.search(customer_id):
        c.display()