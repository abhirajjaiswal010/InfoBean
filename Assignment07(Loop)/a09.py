'''

Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''

n=int(input("Enter The Number : "))
sum=0

while n>0:
    d=n%10
    sum+=d
    n//=10
   
print("All Even" if sum%2==0 else "Not All Even")