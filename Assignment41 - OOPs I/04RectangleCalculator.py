'''
Assignment 4: Rectangle Calculator

A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:
- Length
- Breadth

Create the following methods:
- calculate_area() – Calculate the area.
- calculate_perimeter() – Calculate the perimeter.
- display_result() – Display length, breadth, area, and perimeter.

Formulas:

Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)

Sample data:

Length: 15
Breadth: 8

'''

class Rectangle:
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def calc_area(self):
        return self.length*self.breadth
    
    def calc_peri(self):
        return 2*(self.length+self.breadth)
    
    def display(self):
        print(f"Rectangle Information")
        print(f"Length Of rectangle   : {self.length}")
        print(f"Breadth Of rectangle  : {self.breadth}")
        print(f"Area : {self.calc_area()}")
        print(f"Perimeter : {self.calc_peri()}")


r1=Rectangle(4,2)
r1.display()
    

    
