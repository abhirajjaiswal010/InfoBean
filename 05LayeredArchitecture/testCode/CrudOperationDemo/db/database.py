
import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sql@123",
            database="EmployeeManagementPDBC"
        )

        if connection.is_connected():
            print("Database connected successfully!")

        return connection

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
        return None
