'''

A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
'''
a,b,c,d,e,f=map(int,input("Enter the Stock of 6 unit sperated by Comma(,) : ").split(","))

high=0;

if a>b:
    if a>c:
        if a>d:
            if a>e:
                high=a
            else:
                high=e
        else:
            high=d
    else:
        high=c 
    
else:
    if b>c:
        if b>d:
            if b>e:
                high=b 
            else:
                high=e
        else:
            high=d
    else:
        if c>d:
            if c>e:
                high=c
            else:
                high=e 
        else:
            if d>e:
                high=d 
            else:
                high=e

print(f"Highest Stock : {high}")