
from database import get_connection


def add_employee():

    con = get_connection()
    cur = con.cursor()

    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    city = input("Enter City: ")

    query = """
        INSERT INTO employee_pdbc
        (eid, ename, department, salary, city)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (eid, ename, department, salary, city)

    cur.execute(query, values)

    print("Employee inserted successfully.")

    cur.close()
    con.close()


def display_employees():

    con = get_connection()
    cur = con.cursor()

    query = "SELECT * FROM employee_pdbc"

    cur.execute(query)

    employees = cur.fetchall()

    if employees:

        for employee in employees:
            print(employee)

    else:
        print("No employee records found.")

    cur.close()
    con.close()


def search_employee():

    con = get_connection()
    cur = con.cursor()

    search_name = input("Enter employee name to search: ")

    query = """
        SELECT * FROM employee_pdbc
        WHERE ename LIKE %s
    """

    cur.execute(query, ('%' + search_name + '%',))

    employees = cur.fetchall()

    if employees:

        for employee in employees:
            print(employee)

    else:
        print("No matching employees found.")

    cur.close()
    con.close()


def update_salary():

    con = get_connection()
    cur = con.cursor()

    eid = int(input("Enter Employee ID: "))
    salary = float(input("Enter New Salary: "))

    query = """
        UPDATE employee_pdbc
        SET salary = %s
        WHERE eid = %s
    """

    cur.execute(query, (salary, eid))

    if cur.rowcount > 0:
        print("Employee salary updated successfully.")
    else:
        print("Employee not found or salary unchanged.")

    cur.close()
    con.close()


def delete_employee():

    con = get_connection()
    cur = con.cursor()

    eid = int(input("Enter Employee ID: "))

    query = """
        DELETE FROM employee_pdbc
        WHERE eid = %s
    """

    cur.execute(query, (eid,))

    if cur.rowcount > 0:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

    cur.close()
    con.close()
