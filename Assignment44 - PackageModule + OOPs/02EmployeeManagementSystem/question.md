'''
Create the following structure:

project/
│
├── models/
│   ├── __init__.py
│   └── employee.py
│
└── main.py

IMPORTANT RULES

1. Create the class inside the `models` package.
2. The class must be written in a separate module.
3. Import the class into `main.py`.
4. Create multiple objects of the class.
5. Store all objects inside a list.
6. Perform operations on the list of objects.
7. Take input from the user wherever required.
8. Do not use dictionaries in place of objects.
9. Do not use database connectivity.
10. Display the output in a proper format.

============================================================
ASSIGNMENT 2 – EMPLOYEE MANAGEMENT SYSTEM
=========================================

Create an `Employee` class inside:

models/employee.py

ATTRIBUTES:

* employee_id
* name
* salary
* department

TASKS:

1. Take details of 5 employees from the user.
2. Create Employee objects.
3. Store the objects inside a list.
4. Display all employees.
5. Display employees whose salary is greater than 40,000.
6. Display employees who belong to the IT department.
7. Find the employee having the highest salary.
8. Calculate total salary of all employees.
9. Calculate average salary.

SAMPLE INPUT:

101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

EXPECTED OUTPUT:

All Employees:
101 Amit 45000 IT
102 Rahul 35000 HR
103 Priya 60000 IT
104 Neha 50000 Finance
105 Rohit 30000 HR

Employees with salary greater than 40000:
101 Amit 45000 IT
103 Priya 60000 IT
104 Neha 50000 Finance

Employees from IT Department:
101 Amit 45000 IT
103 Priya 60000 IT

Highest Salary Employee:
103 Priya 60000 IT

Total Salary:
220000

Average Salary:
44000
'''
