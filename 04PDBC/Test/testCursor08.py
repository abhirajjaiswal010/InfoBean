# question -> wrtie a pdbc code to display employee
# whose id is 102,103 or 104 


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

    pattern = input("Enter Pattern: ")

    query = "SELECT * FROM employee"

    cur.execute(query)

    data = cur.fetchall()

    if data:
        for row in data:
            print(row)
    else:
        print("No record found!")

except Error as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()

    if conn and conn.is_connected():
        conn.close()

    print("Connection closed!")
