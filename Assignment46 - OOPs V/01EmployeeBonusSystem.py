"""
Assignment 1 – Employee Bonus System

Create a parent class Employee with the following attributes:

employee_id
employee_name
salary

Create two child classes:

Developer
Manager


Requirements

Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.
Sample Input
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 50000
Enter Employee Type: Developer

Expected Output
----- Employee Details -----
Employee ID   : 101
Employee Name : Rahul
Salary        : 50000
Employee Type : Developer
Bonus         : 5000
Total Amount  : 55000
"""

from rich.prompt import Prompt


class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

    def calculate_bonus(self):
        return 0

    def display(self):

        print("----- Employee Details -----")
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Salary        :", self.salary)


class Developer(Employee):
    def __init__(self, emp_id, emp_name, salary):
        super().__init__(emp_id, emp_name, salary)

    def calculate_bonus(self):
        return self.salary // 10 + (self.salary)

    def display(self):
        super().display()
        bonus = self.calculate_bonus()
        total_amount = self.salary + bonus

        print("Employee Type : Developer")
        print("Bonus         :", bonus)
        print("Total Amount  :", total_amount)


class Manager(Employee):
    def __init__(self, emp_id, emp_name, salary):
        super().__init__(emp_id, emp_name, salary)

    def calculate_bonus(self):
        return self.salary // 5 + (self.salary)

    def display(self):
        super().display()
        bonus = self.calculate_bonus()
        total_amount = self.salary + bonus

        print("Employee Type : Manager")
        print("Bonus         :", bonus)
        print("Total Amount  :", total_amount)


emp_id = int(input("Enter ID : "))
emp_name = input("Enter Name : ")
emp_salary = int(input("Enter salary : "))

print("Choose Employee Type")
print("1.Developer")
print("2.Manager")

choice = Prompt.ask("Choose Number", choices=["1", "2"])


if choice == "1":
    dev = Developer(emp_id, emp_name, emp_salary)
    dev.display()
else:
    man = Manager(emp_id, emp_name, emp_salary)
    man.display()
