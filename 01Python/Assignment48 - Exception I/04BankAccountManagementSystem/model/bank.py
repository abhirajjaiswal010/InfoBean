class BankAccount:
    def __init__(self, account_num, account_holder, balance):
        self.account_num = account_num
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositException("Deposit Amount Cannot Be Negative")

        if amount == 0:
            raise InvalidAmountException("Deposit Amount Must Be Greater Than Zero")

        self.balance += amount
        print(f"Updated Balance : {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidWithdrawalException("Withdrawal Amount Cannot Be Negative")

        if amount == 0:
            raise InvalidAmountException("Withdrawal Amount Must Be Greater Than Zero")

        if amount > self.balance:
            raise InsufficientBalanceException("Insufficient Balance")

        self.balance -= amount
        print(f"Updated Balance : {self.balance}")

    def check_balance(self):
        print(f"Current Balance : {self.balance}")

    def display_account_details(self):
        print(f"Account Number : {self.account_num}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance        : {self.balance}")


class InsufficientBalanceException(Exception):
    pass


class NegativeDepositException(Exception):
    pass


class InvalidWithdrawalException(Exception):
    pass


class InvalidAmountException(Exception):
    pass
