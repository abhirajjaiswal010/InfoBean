from rich.prompt import Prompt
from pathlib import Path as path

base_dir = path(__file__).parent
file_path = base_dir / "emp.txt"


n = int(input("Enter no. of emp : "))

with open(file_path, "w+") as f:

    for i in range(n):
        print(f"\n  {i+1}th Employee Info\n")

        emp_id = input("Enter Employee ID : ")
        emp_name = input("Enter Employee Name : ")
        depart = input("Enter Department : ")
        salary = int(input("Enter Salary : "))

        f.write(f"{emp_id} {emp_name} {depart} {salary} \n")

    f.seek(0)

    employee = f.readlines()

    total_salary = 0

    print("\n Employees With Salary  >  50000\n")

    for i in employee:
        employee_id, employee_name, department, salary = i.split()

        salary = float(salary)

        total_salary += salary

        if salary > 50000:
            print(f"{employee_id} {employee_name} " f"{department} {salary:.0f}")

    average_salary = total_salary / len(employee)

    print(f"\nAverage Salary: {average_salary:.2f}")
