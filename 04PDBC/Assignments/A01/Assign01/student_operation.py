
from database import get_connection


def add_student():

    con = get_connection()
    cur = con.cursor()

    sid = int(input("Enter Student ID: "))
    sname = input("Enter Student Name: ")
    course = input("Enter Course: ")
    fees = float(input("Enter Fees: "))
    city = input("Enter City: ")

    query = """
        INSERT INTO student_pdbc
        (sid, sname, course, fees, city)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (sid, sname, course, fees, city)

    cur.execute(query, values)

    print("Student inserted successfully.")

    cur.close()
    con.close()


def display_students():

    con = get_connection()
    cur = con.cursor()

    query = "SELECT * FROM student_pdbc"

    cur.execute(query)

    students = cur.fetchall()

    if students:
        
        for student in students:
            print(student)
    else:
        print("No student records found.")

    cur.close()
    con.close()


def search_student():

    con = get_connection()
    cur = con.cursor()

    search_name = input("Enter name to search: ")

    query = """
        SELECT * FROM student_pdbc
        WHERE sname LIKE %s
    """

    cur.execute(query, ('%' + search_name + '%',))

    students = cur.fetchall()

    if students:
        
        for student in students:
            print(student)
    else:
        print("No matching students found.")

    cur.close()
    con.close()


def update_fees():

    con = get_connection()
    cur = con.cursor()

    sid = int(input("Enter Student ID: "))
    fees = float(input("Enter New Fees: "))

    query = """
        UPDATE student_pdbc
        SET fees = %s
        WHERE sid = %s
    """

    cur.execute(query, (fees, sid))

    if cur.rowcount > 0:
        print("Student fees updated successfully.")
    else:
        print("Student not found or fees unchanged.")

    cur.close()
    con.close()


def delete_student():

    con = get_connection()
    cur = con.cursor()

    sid = int(input("Enter Student ID: "))

    query = """
        DELETE FROM student_pdbc
        WHERE sid = %s
    """

    cur.execute(query, (sid,))

    if cur.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    cur.close()
    con.close()
