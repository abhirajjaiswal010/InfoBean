'''
Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:
- Employee ID
- Employee name
- Basic salary
- HRA percentage
- DA percentage

Create the following methods:
- calculate_hra() – Calculate HRA.
- calculate_da() – Calculate DA.
- calculate_gross_salary() – Calculate gross salary.
- display_salary() – Display employee salary details.

Formula:

HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA
'''


class Employee:
    id=0
    name=""

    def __init__(self,id,name,salary,hraPercent,DaPercent):
        self.id=id
        self.name=name
        self.salary=salary
        self.hraPercent=hraPercent
        self.DaPercent=DaPercent

    def calc_HRA(self):
        return (self.salary*self.hraPercent)/100
    
    def calc_Da(self):
        return (self.salary*self.DaPercent)/100
    
    def calc_gross(self):
        return float(self.calc_HRA())+float(self.calc_Da())+float(self.salary)
    
    def display(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee Name: {self.name}")
        print(f"Basic Salary: {self.salary}")
        print(f"HRA: {self.calc_HRA()}")
        print(f"DA: {self.calc_Da()}")
        print(f"Gross Salary: {self.calc_gross()}")


e1=Employee(101,"abhi",50000,20,10)
e1.display()