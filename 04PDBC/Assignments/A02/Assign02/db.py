
import mysql.connector as db


def get_connection():
    con = db.connect(
        host="localhost",
        user="root",
        password="sql@123",
        database="officedb",
        autocommit=True
    )
    return con


con = get_connection()

if con.is_connected():
    print("DB Connected Successfully")
    cur = con.cursor()

    # Insert Department Data
    department_query = """
        INSERT IGNORE INTO department_pdbc
        VALUES (%s, %s, %s)
    """

    department = [
        (1, "IT", "Indore"),
        (2, "HR", "Bhopal"),
        (3, "Finance", "Indore"),
        (4, "Sales", "Ujjain"),
        (5, "Training", "Dewas")
    ]

    # Insert Employee Data
    employee_query = """
        INSERT IGNORE INTO employee_pdbc
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    employee = [
        (101, "Amit", 70000.00, "Developer", 1, None),
        (102, "Priya", 55000.00, "Tester", 1, 101),
        (103, "Rahul", 90000.00, "Manager", 1, None),
        (104, "Neha", 45000.00, "HR Executive", 2, None),
        (105, "Karan", 80000.00, "Finance Manager", 3, None),
        (106, "Anjali", 50000.00, "Accountant", 3, 105),
        (107, "Vijay", 40000.00, "Sales Executive", 4, None),
        (108, "Pooja", 60000.00, "Trainer", 5, None)
    ]

    cur.executemany(department_query, department)
    print("Department Data Inserted Successfully")

    cur.executemany(employee_query, employee)
    print("Employee Data Inserted Successfully")

    print("Initial Data Inserted Successfully")

    cur.close()
    con.close()

else:
    print("DB Failed To Connect")
