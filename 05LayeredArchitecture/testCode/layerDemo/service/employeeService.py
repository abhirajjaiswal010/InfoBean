from dao.empDao import EmployeeDao

class EmployeeService:
    def addemployee(self,employee):
        print("Service : processing emp request")
        dao=EmployeeDao()
        dao.saveEmployee(employee)
