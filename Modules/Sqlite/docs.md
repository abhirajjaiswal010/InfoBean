Python sqlite3 Module

sqlite3 is Python's built-in module for working with SQLite databases.

You don't need to install anything.

import sqlite3


1. What is SQLite?

SQLite is a lightweight, file-based relational database.

Unlike MySQL or PostgreSQL, SQLite does not require a separate database server.

Python Program
      ↓
   sqlite3
      ↓
 SQLite Database
      ↓
 database.db

A database is usually stored as a single file:

student.db



connect()	Creates a connection to a database	sqlite3.connect("student.db")
cursor()	Creates a cursor to execute SQL commands	conn.cursor()
execute()	Executes one SQL statement	cursor.execute("SELECT * FROM users")
executemany()	Executes the same SQL statement for multiple records	cursor.executemany(...)
executescript()	Executes multiple SQL statements	cursor.executescript(...)
fetchone()	Fetches one row	cursor.fetchone()
fetchmany()	Fetches a specified number of rows	cursor.fetchmany(3)
fetchall()	Fetches all remaining rows	cursor.fetchall()
commit()	Saves database changes	conn.commit()
rollback()	Cancels uncommitted changes	conn.rollback()
close()	Closes the connection	conn.close()