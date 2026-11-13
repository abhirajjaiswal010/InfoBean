# question -> update salary by asking id and salary from user 



import mysql.connector
from mysql.connector import Error

conn = None
cur = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="sql@123",
        database="pdbcPractise"
    )

    if conn.is_connected():
        print("Database connected successfully!")

    cur = conn.cursor()

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter New Employee Name: ")
    salary = float(input("Enter New Salary: "))

    query = "UPDATE employee SET salary = %s WHERE id = %s"

    cur.execute(query, (salary, emp_id))

    conn.commit()

    print("Record updated successfully!")

except Error as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()

    if conn and conn.is_connected():
        conn.close()

    print("Connection closed!")