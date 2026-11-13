
CREATE DATABASE IF NOT EXISTS a13;

USE a13;

DROP TABLE IF EXISTS employee_project;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS department;

CREATE TABLE department (
    dept_id INT,
    dept_name VARCHAR(30)
);

CREATE TABLE employee (
    emp_id INT,
    emp_name VARCHAR(30),
    salary DECIMAL(10,2),
    dept_id INT,
    manager_id INT
);

CREATE TABLE project (
    project_id INT,
    project_name VARCHAR(50),
    dept_id INT,
    budget INT
);

CREATE TABLE employee_project (
    emp_id INT,
    project_id INT,
    hours_worked INT
);

INSERT INTO department VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Sales'),
(5, 'Marketing'),
(6, 'Research'),
(7, 'Admin');

INSERT INTO employee VALUES
(101, 'Amit', 60000, 1, NULL),
(102, 'Rahul', 50000, 2, 101),
(103, 'Priya', 42000, 2, 101),
(104, 'Neha', 65000, 3, 101),
(105, 'Rohit', 35000, 3, 104),
(106, 'Sneha', 45000, 4, 104),
(107, 'Karan', 55000, 4, 104),
(108, 'Pooja', 30000, 1, 101),
(109, 'Vijay', 75000, 2, 102),
(110, 'Ankit', 32000, 5, 102),
(111, 'Meena', 68000, 3, 104),
(112, 'Arjun', 25000, 5, 110),
(113, 'Tara', 40000, NULL, 102);

INSERT INTO project VALUES
(201, 'Payroll System', 1, 200000),
(202, 'Website Development', 2, 500000),
(203, 'Banking Application', 3, 700000),
(204, 'CRM System', 4, 300000),
(205, 'Inventory System', 5, 150000),
(206, 'AI Research', 6, 900000),
(207, 'Mobile Application', 2, 250000);

INSERT INTO employee_project VALUES
(101, 201, 20),
(102, 202, 40),
(102, 207, 15),
(103, 202, 30),
(104, 203, 35),
(105, 203, 20),
(106, 204, 25),
(107, 204, 30),
(109, 202, 45),
(110, 205, 20),
(111, 203, 25);
