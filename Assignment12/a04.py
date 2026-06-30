'''

Docstring for a04
Question 4: Unique Digit Security Scanner

Write a program using a for-else loop to:

Check whether all digits are unique.
If any digit is repeated, print Invalid Code.
Otherwise, print Valid Unique Code.

Input

57294

Output

Valid Unique Code
'''

n=int(input("Enter The Number : "))
unique=n%10
n//=10
l=len(str(n))
flag=True
for i in range(1,l):
    d=n%10
    if unique==d:
        print("invalid")
        break
    unique=d
    n//=10
else:
    print("valid")
        

