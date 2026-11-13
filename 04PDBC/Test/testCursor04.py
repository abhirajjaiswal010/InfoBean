# question -> wrtie a pdbc code id name salary and insert into the table dynamically


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
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))

    query = "INSERT INTO employee VALUES (%s, %s, %s)"

    cur.execute(query, (emp_id, name, salary))

    conn.commit()

    print("Record inserted successfully!")

except Error as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()

    if conn and conn.is_connected():
        conn.close()

    print("Connection closed!")
