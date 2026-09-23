'''
Docstring for a06
Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

first = input("Enter the first product code: ").lower()
second = input("Enter the second product code: ").lower()

first = first.replace(" ", "")
second = second.replace(" ", "")

if sorted(first) == sorted(second):
    print("Both Product Codes are Matching")
else:
    print("Both Product Codes are Not Matching")
