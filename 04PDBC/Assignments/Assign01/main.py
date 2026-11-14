
from student_operation import (
    add_student,
    display_students,
    search_student,
    update_fees,
    delete_student
)


while True:

    print(" STUDENT MANAGEMENT SYSTEM ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Update Student Fees")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_fees()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice! Please enter a valid choice.")
