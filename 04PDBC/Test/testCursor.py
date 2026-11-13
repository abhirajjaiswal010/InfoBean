
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

    # Execute SELECT query
    cur.execute("SELECT * FROM employee")

    # Fetch all records
    data = cur.fetchall()

    # Display records
    for row in data:
        print(row)

except Error as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()

    if conn and conn.is_connected():
        conn.close()

    print("Connection closed!")
