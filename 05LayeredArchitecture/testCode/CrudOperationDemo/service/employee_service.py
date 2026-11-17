
from dao.employee_dao import EmployeeDAO
from model.employee_model import Employee


class EmployeeService:

    def __init__(self):
        self.employee_dao = EmployeeDAO()

    # 1. CREATE Employee
    def create_employee(self, emp_name, email, department, salary):

        if not emp_name or not email or salary <= 0:
            return None

        employee = Employee(
            None,
            emp_name,
            email,
            department,
            salary
        )

        emp_id = self.employee_dao.create_employee(employee)

        return emp_id

    # 2. READ All Employees
    def get_all_employees(self):

        employees = self.employee_dao.get_all_employees()

        return employees

    # 3. READ Employee By ID
    def get_employee_by_id(self, emp_id):

        if emp_id <= 0:
            return None

        employee = self.employee_dao.get_employee_by_id(emp_id)

        return employee

    # 4. UPDATE Employee
    def update_employee(self, emp_id, emp_name, email, department, salary):

        if emp_id <= 0 or not emp_name or not email or salary <= 0:
            return False

        employee = self.employee_dao.get_employee_by_id(emp_id)

        if employee is None:
            return False

        updated_employee = Employee(
            emp_id,
            emp_name,
            email,
            department,
            salary
        )

        result = self.employee_dao.update_employee(
            emp_id,
            updated_employee
        )

        return result

    # 5. DELETE Employee
    def delete_employee(self, emp_id):

        if emp_id <= 0:
            return False

        employee = self.employee_dao.get_employee_by_id(emp_id)

        if employee is None:
            return False

        result = self.employee_dao.delete_employee(emp_id)

        return result
