'''
Docstring for a07
 Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
'''
n=input("Enter The Number: ")
flag=False
print(n)

if n[0]=='0':
    flag=False
else:
    n1=int(n)
    while n1>0:
       d=n1%10
       if d==0:
        flag=True
        break
       n1//=10


if flag:
    print("duck number")
else:
    print("not duck number")
    
