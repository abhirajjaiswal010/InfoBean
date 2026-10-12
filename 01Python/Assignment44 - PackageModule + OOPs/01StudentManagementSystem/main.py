from models.student import Student


print("-"*5,end="")
print("Student Management System",end="")
print("-"*5)

StudentDb=[]
for i in range(2):

    print(f"Enter {i+1}th Student Info ")
    print()
    roll_no=input("Enter Roll No : ")
    name=input("Enter Name : ")
    marks=input("Enter Marks : ")
    print()

    s=Student(int(roll_no),name,int(marks))
    StudentDb.append(s)

print("-"*5,end="")
print("All Students",end="")
print("-"*5)

for student in StudentDb:
    student.display()

print("-"*5,end="")
print("Student Mark Greater Than 60",end="")
print("-"*5)
for student in StudentDb:
    if student.greater_60():
        student.display()


highest=StudentDb[0]

for student in StudentDb:
    if student.highest_marks(highest):
        highest=student

print()
print("Highest Mark")
highest.display()
print()

average=Student.average(StudentDb)

print(f"Average Marks : {average}")

