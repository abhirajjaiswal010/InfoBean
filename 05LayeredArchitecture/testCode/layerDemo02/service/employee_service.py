from dao.employee_dao import EmployeeDao

class EmployeeService:

    def __init__(self):
        self.dao = EmployeeDao()

    def add_employee(self, emp):

        if emp.salary <= 0:
            print("Invalid Salary")
            return

        self.dao.add_employee(emp)
        print("Employee Added Successfully")

    def get_all_employees(self):

        return self.dao.get_all_employees()