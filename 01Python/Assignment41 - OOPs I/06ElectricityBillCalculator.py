'''
Assignment 6: Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:
- Consumer number
- Consumer name
- Units consumed
- Rate per unit
- Fixed charge

Create the following methods:
- calculate_energy_charge() – Calculate units × rate per unit.
- calculate_total_bill() – Add energy charge and fixed charge.
- display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600
'''

class bill:
    def __init__(self,cName,cNum,cUnit,rps,fixedCharge):
        self.cName=cName
        self.cNum=cNum
        self.cUnit=cUnit
        self.rps=rps
        self.fixedCharge=fixedCharge

    def calc_energy(self):
        return self.rps*self.cUnit
    
    def calc_total(self):
        return self.calc_energy()+self.fixedCharge
    
    
    def display(self):
        print(f"Consumer Number: {self.cNum}")
        print(f"Consumer Name: {self.cName}")
        print(f"Unit Consumed: {self.cUnit}")
        print(f"Rate Per Second: {self.rps}")
        print(f"Fixed Charge: {self.fixedCharge}")
        print(f"Energy Charge: {self.calc_energy()}")
        print(f"Total Bill: {self.calc_total()}")

b1 = bill("Amit", 501, 250, 6, 100)
b1.display()

