'''
Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B
'''
class Student:

    def __init__(self, rollNumber, studentName, marks1, marks2, marks3):
        self.rollNumber = rollNumber
        self.studentName = studentName
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def totalMarks(self):
        return self.marks1+self.marks2+self.marks3

    def percentage(self):
        return self.totalMarks()/3

    def grade(self):

        if self.percentage()>=90:
            return "A"
        elif 75<=self.percentage()<90:
            return "B"
        elif 60<=self.percentage()<75:
            return "C"
        else:
            return "D"
        

    def display(self):
        print("------ Student Result ------")
        print("Roll Number       :", self.rollNumber)
        print("Student Name      :", self.studentName)
        print("Total Marks       :", self.totalMarks())
        print("Percentage        :",round( self.percentage(),2))
        print("Grade             :", self.grade())
        
        


student = Student(101, "Priya Sharma", 85, 90, 88)

student.display()