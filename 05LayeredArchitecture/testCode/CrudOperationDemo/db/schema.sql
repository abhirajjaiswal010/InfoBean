
-- 1. Create Database
CREATE DATABASE EmployeeManagementPDBC;

-- 2. Select Database
USE EmployeeManagementPDBC;

-- 3. Create Employee Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL
);

-- 4. Insert Sample Records
INSERT INTO employees (emp_name, email, department, salary)
VALUES
('Abhiraj', 'abhi@example.com', 'IT', 35000.00),
('Rahul', 'rahul@example.com', 'HR', 28000.00),
('Priya', 'priya@example.com', 'Finance', 40000.00),
('Aman', 'aman@example.com', 'IT', 32000.00);

-- 5. Display All Employees
SELECT * FROM employees;

-- 6. Verify Table Structure
DESC employees;
