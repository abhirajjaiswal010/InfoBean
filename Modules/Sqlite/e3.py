import sqlite3

conn = sqlite3.connect("student1.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

conn.commit()

cursor.execute("""
    INSERT INTO students (name, age)
    VALUES ('Abhiraj', 21)
""")

conn.commit()


cursor.execute("""
    INSERT INTO students (name, age)
    VALUES ('RAJ', 21)
""")

conn.commit()
cursor.execute("SELECT * FROM students")

student = cursor.fetchone()

print(student)

cursor.execute("SELECT * FROM students")

student = cursor.fetchone()

print(student)