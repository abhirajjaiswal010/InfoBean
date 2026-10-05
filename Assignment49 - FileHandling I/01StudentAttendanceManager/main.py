from rich.prompt import Prompt

n = int(input("Enter Student No. "))

with open("attendance.txt", "w+") as f:
    for i in range(n):

        print(f"\nFill {i+1}th info\n")
        name = input("Enter  Name :")
        roll_no = int(input("Enter Roll :"))
        status = Prompt.ask(
            "Choose Status", choices=["Present", "Absent"], case_sensitive=False
        )

        f.write(f"{roll_no} {name} {status}\n")

    f.seek(0)
    student = f.readlines()

    # print(student[0].split())

    total_student = len(student)
    present_count = 0
    absent_count = 0

    for i in student:
        l = i.split()
        status = l[2].lower()

        if status == "present":
            present_count += 1
        else:
            absent_count += 1

    attendance_percent = (present_count / total_student) * 100

    print(f"\nTotal Student   : {total_student}")
    print(f"Present Student : {present_count}")
    print(f"Absent Student  : {absent_count}")
    print(f"Attendance Percent : {attendance_percent:.2f}%")
