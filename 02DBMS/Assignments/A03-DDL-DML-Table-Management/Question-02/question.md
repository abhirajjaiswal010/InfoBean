# Assignment 2 — Library Management System

## Objective

Design and create a Library Management System database in MySQL.

In this assignment, you have to think and decide everything yourself.

You will be given only the requirements. You must decide:

- Database name
- Table names
- Column names
- Data types
- Primary keys
- Auto-increment
- Default values
- Appropriate constraints and data types

## Scenario

A college wants to develop a Library Management System to maintain information about books, students, and book transactions.

### Part 1 — Database Design

Decide and create a database for the Library Management System.

You must decide:

1. An appropriate database name.
2. How many tables are required.
3. The name of each table.
4. The purpose of each table.
5. The relationships between the tables.

### Part 2 — Books Table

The library wants to maintain the following information about books.

| No. | Requirement |
|---:|---|
| 1 | Unique identification of every book |
| 2 | Book title |
| 3 | Author name |
| 4 | ISBN number |
| 5 | Price |
| 6 | Number of available copies |
| 7 | Book category |
| 8 | Publication date |
| 9 | Whether the book is currently available |
| 10 | A short description of the book |

**Task:** Decide appropriate column names, data types, primary keys, auto-increment settings, and constraints.

### Part 3 — Students Table

The library needs to maintain information about registered students.

| No. | Requirement |
|---:|---|
| 1 | Unique identification of every student |
| 2 | Student name |
| 3 | Enrollment/registration number |
| 4 | Age |
| 5 | Gender |
| 6 | Date of birth |
| 7 | Contact number |
| 8 | Email |
| 9 | Whether the student is currently active |
| 10 | Student registration date |

**Task:** Decide appropriate column names, data types, primary keys, auto-increment settings, and constraints.

### Part 4 — Book Issue/Return Table

Whenever a student takes a book from the library, the system must record the transaction.

| No. | Requirement |
|---:|---|
| 1 | Unique identification of each transaction |
| 2 | Which student took the book |
| 3 | Which book was issued |
| 4 | Issue date |
| 5 | Expected return date |
| 6 | Actual return date |
| 7 | Fine amount, if applicable |
| 8 | Whether the book has been returned |
| 9 | Additional remarks |
| 10 | Date and time when the transaction was created |

**Task:** Decide appropriate column names, data types, primary keys, foreign keys, auto-increment settings, and constraints.

### Part 5 — Data Type Selection

Choose the most appropriate MySQL data type for every column.

Consider the following data types wherever appropriate:

- `INT`, `SMALLINT`, `TINYINT`
- `DECIMAL`, `FLOAT`, `DOUBLE`
- `CHAR`, `VARCHAR`
- `TINYTEXT`, `TEXT`
- `ENUM`
- `DATE`, `DATETIME`, `TIMESTAMP`
- `BOOLEAN`

Also decide where to use:

- `PRIMARY KEY`
- `FOREIGN KEY`
- `AUTO_INCREMENT`
- `UNSIGNED`
- `NOT NULL`
- `UNIQUE`
- `DEFAULT`

**Important:** Do not blindly use `VARCHAR` for every column. Choose data types according to the purpose and nature of each field.

### Part 6 — Create Tables (DDL)

Write SQL statements to:

1. Create the database.
2. Select the database.
3. Create the Books table.
4. Create the Students table.
5. Create the Book Issue/Return table.
6. Define appropriate primary keys and foreign keys.
7. Apply suitable constraints and default values.

### Part 7 — Insert Data (DML)

Insert realistic sample data into all tables.

Minimum requirements:

- **Books:** At least 10 records.
- **Students:** At least 10 records.
- **Book Issue/Return:** At least 15 records.

Your data should include different book categories, student details, issue dates, expected return dates, returned and unreturned books, and different fine amounts where applicable.

Ensure that all foreign key values refer to existing records.

### Part 8 — Verification

Execute appropriate SQL statements to verify your database and its contents.

Use:

```sql
SHOW DATABASES;
SHOW TABLES;

DESC books;
DESC students;
DESC book_transactions;

SELECT * FROM books;
SELECT * FROM students;
SELECT * FROM book_transactions;
```

Replace the example table names with your chosen names if they differ.

Verify that:

1. All tables have been created successfully.
2. The required records have been inserted.
3. Primary keys and foreign keys are correctly defined.
4. Data types and constraints match your design.
5. Book transactions are associated with the correct students and books.

## Expected Outcome

By completing this assignment, you should be able to design a relational database independently, select appropriate MySQL data types, apply constraints, establish relationships between tables, create tables using DDL, insert records using DML, and verify the database structure and data.