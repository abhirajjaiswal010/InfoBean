'''

First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5
'''


n=int(input("Enter The Num : "))


while n>0:
    if(len(str(n))==1):
        print(n)
    n//=10
    

    