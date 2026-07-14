'''
Docstring for Assignment18.a07
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''
n=input("Enter Vehicle Number : ")
if len(n)==10:
    a=n[:2]
    b=n[2:4]
    if not a.isalpha():
        print("Not The Alphabets first 2 ")
    if not b.isdigit():
        print("Not the digit ")
    else:
        print("Valid Vehicle Number")
else:
    print("Not leagth 10 ")