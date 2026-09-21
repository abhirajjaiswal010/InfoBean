class Employee:

    def __init__(self,emp_id,emp_name,emp_salary,emp_dept):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_dept=emp_dept

    def display(self):
        print(f"{self.emp_id} {self.emp_name}  Rs.{self.emp_salary}  {self.emp_dept}")

    def is_greater_40k(self):
        return self.emp_salary>40000
            
    
    def belong_it(self):
        return self.emp_dept=="IT"
    
    def highest(self,other):
        return self.emp_salary>other.emp_salary
            
    
    def total_salary(self,total):
        total+=self.emp_salary
        return total
     
    
    def average(self,employee):
        total=0

        for emp in employee:
            total+=emp.emp_salary
        return total/len(employee)
        

