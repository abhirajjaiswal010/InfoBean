class Student:
    

    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks

    def display(self):
        print(f"{self.roll_no} {self.name} {self.marks}")
    
    def greater_60(self):
        return  self.marks>60
    
    def highest_marks(self,other):
        return self.marks>other.marks
    
    @staticmethod
    def average(student):
        total=0

        for std in student:
            total+=std.marks
        return total/len(student)

