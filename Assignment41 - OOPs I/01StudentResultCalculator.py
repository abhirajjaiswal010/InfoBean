'''
Assignment 1: Student Result Calculator

A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:
- Student name
- Roll number
- Marks in English
- Marks in Mathematics
- Marks in Science

Create the following methods:
- calculate_total() – Calculate the total marks.
- calculate_percentage() – Calculate the percentage.
- display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%
'''


class Student:
    name=""
    roll_no=0

    def __init__(self,name,roll_no,english,math,science):
       self.name=name
       self.roll_no=roll_no
       self.english=english
       self.math=math
       self.science=science
    
    def total(self):
        return self.english+self.science+self.math
        

    def percentage(self):
        return self.total()/3
    
    def display(self):
        print(f"Student Name:{self.name}")
        print(f"Roll Number : {self.roll_no}", )
        print(f"Total Marks : {self.total()}", )
        print(f"Percentage  :  {self.percentage()}%")


s1=Student("abhiraj",7,80,70,90)

s1.display()


    