-- Assignment - 02 Solution 
-- question-01 create a database 
CREATE DATABASE company_db;

USE company_db;

-- question-02 Create a Database
CREATE TABLE
    employee (
        employee_id INT PRIMARY KEY AUTO_INCREMENT,
        employee_name VARCHAR(50),
        age INT,
        department VARCHAR(50),
        designation VARCHAR(50),
        salary INT
    );

-- Question 03: Insert values into the table
INSERT INTO
    employee (
        employee_name,
        age,
        department,
        designation,
        salary
    )
VALUES
    ('Rahul Sharma', 28, 'IT', 'Developer', 55000),
    ('Priya Verma', 26, 'HR', 'Executive', 42000),
    ('Amit Singh', 30, 'IT', 'Team Lead', 75000),
    ('Neha Patel', 27, 'Finance', 'Accountant', 48000),
    ('Rohit Mehta', 32, 'IT', 'Manager', 90000),
    ('Sneha Jain', 25, 'Marketing', 'Executive', 40000),
    ('Karan Gupta', 29, 'IT', 'Developer', 60000),
    ('Pooja Mishra', 31, 'HR', 'Manager', 80000),
    ('Ankit Tiwari', 28, 'Finance', 'Analyst', 65000),
    ('Riya Kapoor', 27, 'Marketing', 'Manager', 70000);


-- Question 04: Display the structure
DESC employee;

-- Question 05: Display all records
SELECT * FROM employee;
