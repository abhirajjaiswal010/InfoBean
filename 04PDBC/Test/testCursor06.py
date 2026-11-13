# question -> deletion operation
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

    emp_id = int(input("Enter Employee ID to Delete: "))

    query = "DELETE FROM employee WHERE id = %s"

    cur.execute(query, (emp_id,))

    conn.commit()

    print("Record deleted successfully!")

except Error as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()

    if conn and conn.is_connected():
        conn.close()

    print("Connection closed!")
