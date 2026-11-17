from db.database import get_connection

class EmployeeDao:

    def add_employee(self, emp):

        con = get_connection()
        cur = con.cursor()

        query = """
        INSERT INTO employee
        VALUES (%s, %s, %s, %s)
        """

        values = (
            emp.eid,
            emp.ename,
            emp.department,
            emp.salary
        )

        cur.execute(query, values)
        con.commit()

        cur.close()
        con.close()

    def get_all_employees(self):

        con = get_connection()
        cur = con.cursor()

        cur.execute("SELECT * FROM employee")

        result = cur.fetchall()

        cur.close()
        con.close()

        return result