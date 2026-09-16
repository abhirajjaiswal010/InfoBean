import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE students (
        id INTEGER,
        name TEXT,
        age INTEGER
    )
""")
conn.commit()