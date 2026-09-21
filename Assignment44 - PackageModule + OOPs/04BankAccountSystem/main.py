from models.account import Account

print("-" * 20)
print("BANK ACCOUNT SYSTEM")
print("-" * 20)

accountDB = []

for i in range(3):

    print()
    print(f"Enter Account {i + 1} Details")
    print("-" * 30)

    account_no = int(input("Enter Account No : "))
    customer_name = input("Enter Customer Name : ")
    balance = int(input("Enter Balance : "))

    account = Account(account_no, customer_name, balance)
    accountDB.append(account)


print()
print("-" * 20)
print("ALL ACCOUNTS")
print("-" * 20)

for account in accountDB:
    account.display()


print()
print("-" * 20)
print("SEARCH ACCOUNT")
print("-" * 20)

search_no = int(input("Enter Account No : "))

found = False

for account in accountDB:
    if account.account_no == search_no:
        account.display()
        print("Account Found")
        found = True
        break

if not found:
    print("Account Not Found")


print()
print("-" * 20)
print("DEPOSIT MONEY")
print("-" * 20)

deposit_no = int(input("Enter Account No : "))

found = False

for account in accountDB:
    if account.account_no == deposit_no:

        amount = int(input("Enter Amount To Deposit : "))

        account.deposit(amount)

        print()
        print("After Deposit:")
        account.display()

        found = True
        break

if not found:
    print("Account Not Found")


print()
print("-" * 20)
print("WITHDRAW MONEY")
print("-" * 20)

withdraw_no = int(input("Enter Account No : "))

found = False

for account in accountDB:
    if account.account_no == withdraw_no:

        amount = int(input("Enter Amount To Withdraw : "))

        account.withdraw(amount)

        print()
        print("After Withdrawal:")
        account.display()

        found = True
        break

if not found:
    print("Account Not Found")


print()
print("-" * 20)
print("BALANCE GREATER THAN 20,000")
print("-" * 20)

for account in accountDB:
    if account.balance > 20000:
        account.display()


print()
print("-" * 20)
print("HIGHEST BALANCE ACCOUNT")
print("-" * 20)

highest = accountDB[0]

for account in accountDB:
    if account.balance > highest.balance:
        highest = account

highest.display()