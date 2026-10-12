class Account:

    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        print(f"{amount} is credited to your account")

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} debited from your account")
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"{self.account_no} {self.customer_name} {self.balance}")