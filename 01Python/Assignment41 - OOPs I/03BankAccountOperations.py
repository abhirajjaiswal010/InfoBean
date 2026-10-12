'''
Assignment 3: Bank Account Operations

A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:
- Account number
- Account holder name
- Balance

Create the following methods:
- deposit() – Add an amount to the balance.
- withdraw() – Subtract an amount from the balance.
- display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000
'''

class BankAccount:

    account_no = 0
    name = ""
    balance = 0

    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display_account(self):
        print(f"Account Number: {self.account_no}")
        print(f"Account Holder: {self.name}")
        print(f"Final Balance: {self.balance}")


account1 = BankAccount(1001, "Rahul", 25000)

account1.deposit(5000)
account1.withdraw(3000)

account1.display_account()
    
