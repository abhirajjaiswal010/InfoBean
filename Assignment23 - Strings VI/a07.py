'''
Docstring for Assignment23 - String VI.a06
Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

Write a Python program to check whether a password is strong based on the following conditions:

Conditions:
• Minimum 10 characters
• At least one uppercase letter
• At least one lowercase letter
• At least one digit
• At least one special character
• No consecutive repeating characters
• No spaces allowed

If all conditions are satisfied, print:

Strong Password

Otherwise, print:

Weak Password

Input:
Pyth@n1234

Output:
Strong Password

Input:
Paaass@12

Output:
Weak Password
'''
n = input("Enter Password : ")

upper = False
lower = False
digit = False
special = False
space = False
repeat = False

# Password ke har character ko check karo
for i in range(len(n)):

    # Uppercase character check
    if n[i].isupper():
        upper = True

    # Lowercase character check
    elif n[i].islower():
        lower = True

    # Digit check
    elif n[i].isdigit():
        digit = True

    # Space check
    elif n[i] == " ":
        space = True

    # Jo uppercase/lowercase/digit/space nahi hai
    # use special character maan rahe hain
    else:
        special = True

    # Consecutive same characters check
    if i > 0 and n[i] == n[i - 1]:
        repeat = True


# Saari conditions check karo
if (len(n) >= 10 and
    upper and
    lower and
    digit and
    special and
    not space and
    not repeat):

    print("Strong Password")

else:
    print("Weak Password")