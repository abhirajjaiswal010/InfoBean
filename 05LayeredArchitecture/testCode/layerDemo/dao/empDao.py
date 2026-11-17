from db.connection import Database
class EmployeeDao:
    def saveEmployee(self,employee):
        print("DAO:saving employee data")
        print("ID :",employee.id)
        print("Name : ",employee.name)
        print("Salary : ",employee.salary)
        db=Database()
        db.connect()