from tabulate import tabulate
from service.employee_service import EmployeeService


def main():

    employee_service = EmployeeService()

    while True:

        print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. View Employee By ID")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        # 1. CREATE Employee
        if choice == "1":

            print("\n--- ADD EMPLOYEE ---")

            emp_name = input("Enter employee name: ")
            email = input("Enter email: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))

            emp_id = employee_service.create_employee(
                emp_name, email, department, salary
            )

            if emp_id:
                print("\nEmployee added successfully!")
                print("Employee ID:", emp_id)
            else:
                print("\nEmployee not added!")

        # 2. READ All Employees
        elif choice == "2":

            print("\n--- ALL EMPLOYEES ---")

            employees = employee_service.get_all_employees()

            if not employees:
                print("No employees found.")

            else:
                header=["Emp_id","Emp_Name","Emp_Email","Department","Salary"]
                data=[]
                for emp in employees:
                    data.append([
                        emp.emp_id,
                        emp.emp_name,
                        emp.email,
                        emp.department,
                        emp.salary


                    ])
                
                print(tabulate(data,headers=header,tablefmt="rounded_grid"))

        # 3. READ Employee By ID
        elif choice == "3":

            print("\n--- SEARCH EMPLOYEE ---")

            emp_id = int(input("Enter employee ID: "))

            emp = employee_service.get_employee_by_id(emp_id)

            if emp is None:
                print("Employee not found!")

            else:
                print("\nEmployee Found!")
                print("ID:", emp.emp_id)
                print("Name:", emp.emp_name)
                print("Email:", emp.email)
                print("Department:", emp.department)
                print("Salary:", emp.salary)

        # 4. UPDATE Employee
        elif choice == "4":

            print("\n--- UPDATE EMPLOYEE ---")

            emp_id = int(input("Enter employee ID: "))

            emp = employee_service.get_employee_by_id(emp_id)

            if emp is None:
                print("Employee not found!")

            else:
                print("\nEnter Updated Details")

                emp_name = input("Enter new name: ")
                email = input("Enter new email: ")
                department = input("Enter new department: ")
                salary = float(input("Enter new salary: "))

                result = employee_service.update_employee(
                    emp_id, emp_name, email, department, salary
                )

                if result:
                    print("Employee updated successfully!")
                else:
                    print("Employee update failed!")

        # 5. DELETE Employee
        elif choice == "5":

            print("\n--- DELETE EMPLOYEE ---")

            emp_id = int(input("Enter employee ID: "))

            result = employee_service.delete_employee(emp_id)

            if result:
                print("Employee deleted successfully!")
            else:
                print("Employee deletion failed!")

        # 6. EXIT
        elif choice == "6":

            print("\nThank you for using Employee Management System!")
            break

        else:
            print("\nInvalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()
