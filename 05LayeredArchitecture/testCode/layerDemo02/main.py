from model.employee import Employee
from service.employee_service import EmployeeService

service = EmployeeService()

while True:

    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        eid = int(input("Enter ID: "))
        ename = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(eid, ename, department, salary)

        service.add_employee(emp)

    elif choice == "2":

        employees = service.get_all_employees()

        for emp in employees:
            print(emp)

    elif choice == "3":
        print("Application Closed")
        break

    else:
        print("Invalid Choice")