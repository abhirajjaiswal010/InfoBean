from service.employeeService import EmployeeService
from model.employee import Employee

print("Welcome")
# service=EmployeeService()
# service.getemployee()

emp=Employee(101,"Deepika",5000)
service=EmployeeService()   
service.addemployee(emp)