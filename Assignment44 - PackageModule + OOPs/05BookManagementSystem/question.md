'''
Create the following structure:

project/
│
├── models/
│   ├── __init__.py
│   └── book.py
│
└── main.py

IMPORTANT RULES

1. Create the class inside the `models` package.
2. The class must be written in a separate module.
3. Import the class into `main.py`.
4. Create multiple objects of the class.
5. Store all objects inside a list.
6. Perform operations on the list of objects.
7. Take input from the user wherever required.
8. Do not use dictionaries in place of objects.
9. Do not use database connectivity.
10. Display the output in a proper format.

============================================================
ASSIGNMENT 5 – BOOK MANAGEMENT SYSTEM
=====================================

Create a `Book` class inside:

models/book.py

ATTRIBUTES:

* book_id
* book_name
* author
* price

TASKS:

1. Take details of 5 books from the user.
2. Create Book objects.
3. Store all Book objects in a list.
4. Display all books.
5. Search a book using Book Id.
6. Display all books written by a particular author.
7. Display books whose price is greater than 500.
8. Find the most expensive book.
9. Calculate average price of all books.

SAMPLE INPUT:

101 Java Programming James 650
102 Python Basics Mark 550
103 MySQL Guide John 450
104 Advanced Java James 800
105 DSA in Python Robert 700

EXPECTED OUTPUT:

All Books:
101 Java Programming James 650
102 Python Basics Mark 550
103 MySQL Guide John 450
104 Advanced Java James 800
105 DSA in Python Robert 700

Books by James:
101 Java Programming 650
104 Advanced Java 800

Books with price greater than 500:
Java Programming
Python Basics
Advanced Java
DSA in Python

Most Expensive Book:
Advanced Java = 800

Average Price:
630
'''
