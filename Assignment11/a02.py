'''
Docstring for a02
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''

n=int(input("Enter The Number : "))
count=n+1
flag=True
ans=0

while count<(n*2):
    i=2
    while i*i<=count:
        if count%i==0:
            flag=False
            break
        i+=1
    if flag:
        ans=count
        break
    else:
        flag=True
        count+=1

print(f"next prime : {ans}")

    
            
