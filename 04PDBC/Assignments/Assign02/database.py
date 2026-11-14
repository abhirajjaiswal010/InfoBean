import mysql.connector as db


def get_connection():

    con = db.connect(
        host="localhost",
        user="root",
        password="sql@123",
        database="pdbcAssign02",
        autocommit=True,
    )

    return con


con = get_connection()

if con.is_connected():
    print("DB is connected successfully")

    cur = con.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS 
         employee_pdbc (
            eid INT PRIMARY KEY,
            ename VARCHAR(50),
            department VARCHAR(50),
            salary DECIMAL(10,2),
            city VARCHAR(30)
        )
    """

    cur.execute(query)

    InsertQuery = """
        INSERT ignore INTO employee_pdbc (eid, ename, department, salary, city)
        VALUES (%s, %s, %s, %s, %s)
    """

    employees = [
        (201, "Amit", "IT", 45000.00, "Indore"),
        (202, "Priya", "HR", 40000.00, "Bhopal"),
        (203, "Rahul", "IT", 55000.00, "Indore"),
        (204, "Neha", "Finance", 50000.00, "Ujjain"),
        (205, "Karan", "IT", 60000.00, "Indore"),
    ]

    cur.executemany(InsertQuery, employees)

    print(cur.rowcount, "employees inserted successfully")

    cur.close()
    con.close()

else:
    print("DB is not connected")
