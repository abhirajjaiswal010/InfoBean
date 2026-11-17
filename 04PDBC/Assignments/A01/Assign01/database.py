
import mysql.connector as db

def get_connection():

    con = db.connect(
        host="localhost",
        user="root",
        password="sql@123",
        database="pdbcAssign01",
        autocommit=True
    )

    return con

con=get_connection()

if con.is_connected():
    print("DB is connected successfully")

    cur = con.cursor()

    
    query = """
        CREATE TABLE IF NOT EXISTS student_pdbc (
            sid INT PRIMARY KEY,
            sname VARCHAR(50),
            course VARCHAR(50),
            fees DECIMAL(10,2),
            city VARCHAR(30)
        )
    """

    cur.execute(query)

   
    InsertQuery = """
        INSERT ignore INTO student_pdbc (sid, sname, course, fees, city)
        VALUES (%s, %s, %s, %s, %s)
    """

    students = [
        (101, "Amit", "Python", 15000.00, "Indore"),
        (102, "Priya", "Java", 18000.00, "Bhopal"),
        (103, "Rahul", "Python", 15000.00, "Indore"),
        (104, "Neha", "Java", 18000.00, "Ujjain"),
        (105, "Karan", "MERN", 20000.00, "Indore")
    ]

    cur.executemany(InsertQuery, students)

    print(cur.rowcount, "students inserted successfully")

    cur.close()
    con.close()

else:
    print("DB is not connected")
