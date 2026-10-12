'''
Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
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


e1=Employee(101,"abhi",50000,20,15)
e1.display()