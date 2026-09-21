'''
Create the following structure:

project/
│
├── models/
│   ├── __init__.py
│   └── customer.py
│
└── main.py

IMPORTANT RULES

1. Create the class inside the `models` package.
2. The class must be written in a separate module.
3. Import the class into `main.py`.
4. Create multiple objects of the class.
5. Store all objects inside a list.
6. Perform operations on the list of objects.
7. Take input from the user wherever required.
8. Do not use dictionaries in place of objects.
9. Do not use database connectivity.
10. Display the output in a proper format.

============================================================
ASSIGNMENT 6 – CUSTOMER MANAGEMENT SYSTEM
=========================================

Create a `Customer` class inside:

models/customer.py

ATTRIBUTES:

* customer_id
* customer_name
* city
* purchase_amount

TASKS:

1. Take details of 5 customers.
2. Create Customer objects.
3. Store all objects in a list.
4. Display all customers.
5. Display customers from a particular city.
6. Display customers whose purchase amount is greater than 10,000.
7. Find the customer having the highest purchase amount.
8. Calculate total sales.
9. Calculate average purchase amount.
10. Search customer using Customer Id.

SAMPLE DATA:

101 Amit Indore 12000
102 Rahul Bhopal 8000
103 Priya Indore 15000
104 Neha Pune 22000
105 Rohit Indore 7000

EXPECTED OUTPUT:

Customers from Indore:

101 Amit 12000
103 Priya 15000
105 Rohit 7000

Customers with purchase amount greater than 10000:

101 Amit 12000
103 Priya 15000
104 Neha 22000

Highest Purchase Customer:

104 Neha 22000

Total Sales:

64000

Average Purchase Amount:

12800

Search Customer Id: 103

Customer Found:

103 Priya Indore 15000
'''
