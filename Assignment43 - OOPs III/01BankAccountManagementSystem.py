class Bank:

    bank_name = "ABC Bank"
    interest_rate = 7.5
    transaction_id = 1000

    def __init__(self, account_num, customer_name, account_balance):
        self.account_num = account_num
        self.customer_name = customer_name
        self.account_balance = account_balance

    # Instance Methods

    def deposit_money(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw_money(self, amount):
        self.account_balance -= amount
        return self.account_balance

    def display_account_info(self):
        print(f"Account Number  : {self.account_num}")
        print(f"Customer Name   : {self.customer_name}")
        print(f"Account Balance : {self.account_balance}")
        print()

    def transfer_money(self, receiver, amount):
        if amount <= 0:
            print("Invalid Amount")

        elif self.account_balance >= amount:
            self.account_balance -= amount
            receiver.account_balance += amount

            print(f"Transfer Successfully to {receiver.customer_name}")

        else:
            print("Not Enough Balance")

    # Class Methods

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @classmethod
    def display_bank_info(cls):
        print(f"Bank Name      : {cls.bank_name}")
        print(f"Interest Rate  : {cls.interest_rate}%")
        print()

    # Static Methods

    @staticmethod
    def validate_account_number(account_no):
        if 1000 <= account_no <= 9999:
            print("Valid Account Number")
        else:
            print("Invalid Account Number")

    @staticmethod
    def calculate_interest(amount, rate):
        interest = (amount * rate) / 100
        print(f"Interest : {interest}")

    @staticmethod
    def generate_transaction_id():
        Bank.transaction_id += 25
        transaction_id = "TXN" + str(Bank.transaction_id)
        print(f"Transaction ID : {transaction_id}")


# Program

Bank.display_bank_info()

deepika = Bank(1002, "Deepika", 30000)
deepika.display_account_info()

priya = Bank(1003, "Priya", 2000)
priya.display_account_info()

deepika.transfer_money(priya, 3000)

print("\nAfter Transfer:")

deepika.display_account_info()
priya.display_account_info()

Bank.validate_account_number(1002)

Bank.calculate_interest(30000, 7.5)

Bank.generate_transaction_id()