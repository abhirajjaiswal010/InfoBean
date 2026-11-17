
from employee_operation import (
    add_employee,
    display_employees,
    search_employee,
    update_salary,
    delete_employee
)


while True:

    print("EMPLOYEE MANAGEMENT SYSTEM ")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee by Name")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        display_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        update_salary()

    elif choice == 5:
        delete_employee()

    elif choice == 6:
        print("Thank you for using Employee Management System.")
        break

    else:
        print("Invalid choice! Please enter a valid choice.")
