
CREATE DATABASE IF NOT EXISTS joinAssign;

USE joinAssign;

-- Create Department Table
CREATE TABLE IF NOT EXISTS department
(
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(40)
);

-- Create Employee Table
CREATE TABLE IF NOT EXISTS employee
(
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(40),
    dept_id INT

    
);

-- Insert Department Records
INSERT INTO department (dept_id, dept_name)
VALUES
(101, 'HR'),
(102, 'IT'),
(104, 'Finance');

-- Insert Employee Records
INSERT INTO employee (emp_id, emp_name, dept_id)
VALUES
(1, 'Alice', 101),
(2, 'Bob', 102),
(3, 'Charlie', 103),
(4, 'David', 101);

-- Display Records
SELECT * FROM department;

SELECT * FROM employee;
