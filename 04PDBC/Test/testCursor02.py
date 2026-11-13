# question-02 --> write a pdbc program read name from user and display all the record with given name 


import mysql.connector
from mysql.connector import Error

conn = None
cur = None

try:
    # Establish connection
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="sql@123",
        database="pdbcPractise"
    )

    if conn.is_connected():
        print("Database connected successfully!")

    # Create cursor
    cur = conn.cursor()

    userName=input("Enter User Name ")
    query = "SELECT * FROM employee WHERE name = %s"

    cur.execute(query,(userName,))
    data=cur.fetchall()

    if data:
        for row in data:
            print(row)
        print("User Found")
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
