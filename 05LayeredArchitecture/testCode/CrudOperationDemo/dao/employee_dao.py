
from db.database import get_connection
from model.employee_model import Employee


class EmployeeDAO:

    # 1. CREATE Employee
    def create_employee(self, employee):

        connection = get_connection()

        if connection is None:
            return None

        cursor = connection.cursor()

        query = """
            INSERT INTO employees
            (emp_name, email, department, salary)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            employee.emp_name,
            employee.email,
            employee.department,
            employee.salary
        )

        cursor.execute(query, values)
        connection.commit()

        emp_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return emp_id

    # 2. READ All Employees
    def get_all_employees(self):

        connection = get_connection()

        if connection is None:
            return []

        cursor = connection.cursor()

        query = "SELECT * FROM employees"

        cursor.execute(query)

        rows = cursor.fetchall()

        employees = []

        for row in rows:

            employee = Employee(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )

            employees.append(employee)

        cursor.close()
        connection.close()

        return employees

    # 3. READ Employee By ID
    def get_employee_by_id(self, emp_id):

        connection = get_connection()

        if connection is None:
            return None

        cursor = connection.cursor()

        query = "SELECT * FROM employees WHERE emp_id = %s"

        cursor.execute(query, (emp_id,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row is None:
            return None

        employee = Employee(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )

        return employee

    # 4. UPDATE Employee
    def update_employee(self, emp_id, employee):

        connection = get_connection()

        if connection is None:
            return False

        cursor = connection.cursor()

        query = """
            UPDATE employees
            SET emp_name = %s,
                email = %s,
                department = %s,
                salary = %s
            WHERE emp_id = %s
        """

        values = (
            employee.emp_name,
            employee.email,
            employee.department,
            employee.salary,
            emp_id
        )

        cursor.execute(query, values)
        connection.commit()

        result = cursor.rowcount > 0

        cursor.close()
        connection.close()

        return result

    # 5. DELETE Employee
    def delete_employee(self, emp_id):

        connection = get_connection()

        if connection is None:
            return False

        cursor = connection.cursor()

        query = "DELETE FROM employees WHERE emp_id = %s"

        cursor.execute(query, (emp_id,))
        connection.commit()

        result = cursor.rowcount > 0

        cursor.close()
        connection.close()

        return result
