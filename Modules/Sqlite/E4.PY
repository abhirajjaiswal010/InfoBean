import sqlite3

conn = sqlite3.connect("student2.db")
cursor = conn.cursor()

# CREATE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

# INSERT
cursor.execute("""
    INSERT INTO students (name, age)
    VALUES (?, ?)
""", ("Abhiraj", 21))

# READ
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

# UPDATE
cursor.execute("""
    UPDATE students
    SET age = ?
    WHERE name = ?
""", (22, "Abhiraj"))

# DELETE
cursor.execute("""
    DELETE FROM students
    WHERE name = ?
""", ("Abhiraj",))

conn.commit()

conn.close()