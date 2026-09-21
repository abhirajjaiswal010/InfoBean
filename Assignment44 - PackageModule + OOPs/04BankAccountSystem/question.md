'''
Create the following structure:

project/
│
├── models/
│   ├── __init__.py
│   └── account.py
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
ASSIGNMENT 4 – BANK ACCOUNT SYSTEM
==================================

Create an `Account` class inside:

models/account.py

ATTRIBUTES:

* account_no
* customer_name
* balance

METHODS:

* deposit()
* withdraw()
* display()

TASKS:

1. Create 5 Account objects.
2. Store all Account objects in a list.
3. Display all accounts.
4. Search an account using Account Number.
5. Deposit money into a selected account.
6. Withdraw money from a selected account.
7. Display accounts having balance greater than 50,000.
8. Find the account having the highest balance.

SAMPLE DATA:

101 Amit 45000
102 Rahul 75000
103 Priya 35000
104 Neha 90000
105 Rohit 55000

SAMPLE OPERATIONS:

Enter Account No: 101

Enter amount to deposit: 10000

After Deposit:
101 Amit 55000

Enter Account No: 103

Enter amount to withdraw: 5000

After Withdrawal:
103 Priya 30000

EXPECTED OUTPUT:

Accounts having balance greater than 50000:

102 Rahul 75000
104 Neha 90000
105 Rohit 55000

Highest Balance Account:

104 Neha 90000
'''
