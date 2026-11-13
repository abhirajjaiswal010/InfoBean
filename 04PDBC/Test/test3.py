# Question -> write a pdbc program to read data from user and insert into the table .


import mysql.connector
from mysql.connector import Error

try:
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sql@123",
        database="pdbcPractise"
    )

    print("Database connected successfully!")

    
    cur = conn.cursor()

    n=int(input("Enter Number of Emp : "))
    data=[]
    for i in range(n):

        emp_id = int(input("Enter Employee ID: "))
        emp_name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        data.append((emp_id,emp_name,salary))

    # Insert query
    query = "INSERT INTO employee VALUES (%s, %s, %s)"

    # Execute query
    cur.executemany(query, data)

    # Save changes
    conn.commit()

    print("Record inserted successfully!")

except Error as e:
    print("Error:", e)

finally:
    if 'cur' in locals():
        cur.close()

    if 'conn' in locals() and conn.is_connected():
        conn.close()

    print("Connection closed!")
