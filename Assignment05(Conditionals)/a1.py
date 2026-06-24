'''
1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250 100->101

Output:
Total Electricity Bill: ₹1950

'''

unit=int(input("Enter The Unit : "))
charge=0;

for i in (100,unit+1):
    if unit==100:
        charge=(unit*5)
    elif unit>=101 and unit<=200:
        charge+=(unit*7)
    else:
        charge+=(unit*10)

print(charge)
        