
from operation import *

while True:

    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Department")
    print("2. Add Employee")
    print("3. Display All Employees")
    print("4. Search Employee")
    print("5. Update Employee Salary")
    print("6. Update Employee Department")
    print("7. Delete Employee")
    print("8. Department Employee Count")
    print("9. Department Average Salary")
    print("10. Employees Earning More Than Average")
    print("11. Employees Earning More Than Department Average")
    print("12. Employees Working in IT")
    print("13. Departments Having More Than One Employee")
    print("14. Display Employee and Manager")
    print("15. Departments With No Employees")
    print("16.Test foreign key contraint")
    print("17. Exit")

    choice = int(input("\nEnter Your Choice: "))

    match choice:

        case 1:
            addDepartment()

        case 2:
            addEmployee()

        case 3:
            displayAll()

        case 4:
            searchEmp()

        case 5:
            updateEmployeeSalary()

        case 6:
            updateEmployeeDept()

        case 7:
            deleteEmployee()

        case 8:
            displayDeptEmpCount()

        case 9:
            displayDeptAvgSalary()

        case 10:
            EmpEarningMoreAvgSalary()

        case 11:
            empEarnMoreDeptAvg()

        case 12:
            displayEmpWorkAtIT()

        case 13:
            displayDeptMoreOneEmp()

        case 14:
            displayEmpManager()

        case 15:
            displayDeptWithNoEmp()

        case 16:
            checkForeignKeyConstraint()

        case 17:
            print("Thank You! Application Closed.")
            break

        case _:
            print("Invalid Choice!")
