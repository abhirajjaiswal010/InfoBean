'''
Assignment 3 – Bank Account System

Create a parent class BankAccount with:

account_no
holder_name
balance

Create two child classes:

SavingsAccount
CurrentAccount
Requirements
Take account details from the user.
Use super() to initialize the common attributes.
Create a method calculate_interest() in the parent class.
Override this method in both child classes.
Savings Account gets 5% interest.
Current Account gets 2% interest.
Display the account details and calculated interest.
Sample Input
Enter Account Number: 1001
Enter Holder Name: Amit
Enter Balance: 50000
Enter Account Type: Savings


Expected Output
----- Account Details -----
Account Number : 1001
Holder Name    : Amit
Balance        : 50000
Account Type   : Savings
Interest Rate  : 5%
Interest       : 2500
Amount After Interest : 52500
'''
