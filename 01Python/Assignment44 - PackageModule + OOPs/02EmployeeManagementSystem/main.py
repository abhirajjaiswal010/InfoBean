from models.employee import Employee


print("-" * 20)
print("Employee Management System")
print("-" * 20)

empDb = []

for i in range(3):

    print(f"Enter {i + 1}th Employee Info")

    emp_id = input("Enter ID : ")
    name = input("Enter Name : ")
    salary = int(input("Enter Salary : "))

    print("Select Department")
    print("1. IT")
    print("2. HR")
    print("3. Finance")
    print("4. Marketing")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        dept = "IT"
    elif choice == 2:
        dept = "HR"
    elif choice == 3:
        dept = "Finance"
    elif choice == 4:
        dept = "Marketing"
    else:
        print("Invalid Choice")
        dept = "Unknown"

    emp = Employee(emp_id, name, salary, dept)
    empDb.append(emp)

    print()


print("-" * 20)
print("All Employees List")
print("-" * 20)

for employee in empDb:
    employee.display()


print()
print("-" * 20)
print("Employees Salary > Rs. 40,000")
print("-" * 20)

for employee in empDb:
    if employee.is_greater_40k():
        employee.display()


print()
print("-" * 20)
print("Employee Belong From IT")
print("-" * 20)

for employee in empDb:
    if employee.belong_it():
        employee.display()


print()
print("-" * 20)
print("Highest Salary")
print("-" * 20)

high = empDb[0]

for employee in empDb:
    if employee.highest(high):
        high = employee

high.display()


print()
print("-" * 20)
print("Total Salary")
print("-" * 20)

total = 0

for employee in empDb:
    total = employee.total_salary(total)

print(total)


print()
print("-" * 20)
print("Average Salary")
print("-" * 20)

avg = empDb[0].average(empDb)

print(f"{avg:.2f}")

print("---End---")