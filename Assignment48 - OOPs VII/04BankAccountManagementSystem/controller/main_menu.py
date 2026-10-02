from model.bank import (
    BankAccount,
    InsufficientBalanceException,
    InvalidAmountException,
    InvalidWithdrawalException,
    NegativeDepositException,
)


def main_menu():

    account_num = int(input("Enter Account Number : "))
    account_holder = input("Enter Account Holder : ")
    balance = int(input("Enter Account Balance : "))

    acc1 = BankAccount(account_num, account_holder, balance)

    while True:
        print("""
================================
BANK ACCOUNT SYSTEM
===================

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit""")

        choice = int(input("Enter Choice :"))

        match choice:
            case 1:
                print("\n   Deposit Amount\n")
                amount = int(input("Enter Amount : "))

                try:
                    acc1.deposit(amount)
                except NegativeDepositException as e:
                    print(f"NegativeDepositException : {e}")
                except InvalidAmountException as e:
                    print(f"InvalidAmountException : {e}")
            case 2:
                print("\n   Withdraw Amount\n")
                amount = int(input("Enter Amount : "))

                try:
                    acc1.withdraw(amount)
                except InsufficientBalanceException as e:
                    print(f"InsufficientBalanceException : {e}")
                except InvalidAmountException as e:
                    print(f"InvalidAmountException : {e}")
                except InvalidWithdrawalException as e:
                    print(f"InvalidWithdrawalException : {e}")
            case 3:
                print("\n   Check Balance\n")
                print("Current Balance \n")
                acc1.check_balance()
            case 4:
                print("\n   Display Account Detail Amount\n")
                acc1.display_account_details()
            case 5:
                print("Existing ...")
                break
            case _:
                print("invalid choice")
