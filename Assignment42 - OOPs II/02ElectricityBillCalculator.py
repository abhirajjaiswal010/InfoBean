"""
Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0
"""


class bill:
    def __init__(self, cName, cNum, cUnit, fixedCharge):
        self.cName = cName
        self.cNum = cNum
        self.cUnit = cUnit

        self.fixedCharge = fixedCharge

    def calc_energy(self):
        return 8 * self.cUnit

    def calc_total(self):
        return self.calc_energy() + self.fixedCharge

    def display(self):
        print(f"Consumer Number : {self.cNum}")
        print(f"Consumer Name   : {self.cName}")
        print(f"Unit Consumed   : {self.cUnit}")
        print(f"Fixed Charge    : {self.fixedCharge}")
        print(f"Total Bill      : {self.calc_total()}")


b1 = bill("Amit", 501, 350, 150)
b1.display()
