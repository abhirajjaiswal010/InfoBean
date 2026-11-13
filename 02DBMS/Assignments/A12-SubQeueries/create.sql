CREATE DATABASE if NOT EXISTS a12;
use  a12;

CREATE TABLE if NOT EXISTS department
(
    dept_id int,
    dept_name varchar(30),
    location varchar(30)
);

CREATE TABLE if NOT EXISTS employee
(
    emp_id int,
    emp_name VARCHAR(30),
    salary decimal(10,2),
    dept_id INT 
);

INSERT INTO department (dept_id, dept_name, location)
VALUES
(1, 'HR', 'Indore'),
(2, 'IT', 'Pune'),
(3, 'Finance', 'Mumbai'),
(4, 'Sales', 'Indore'),
(5, 'Admin', 'Delhi'),
(6, 'Research', 'Bangalore');

INSERT INTO employee (emp_id, emp_name, salary, dept_id)
VALUES
(101, 'Amit', 30000.00, 1),
(102, 'Rahul', 50000.00, 2),
(103, 'Priya', 40000.00, 2),
(104, 'Neha', 60000.00, 3),
(105, 'Rohit', 35000.00, 3),
(106, 'Sneha', 45000.00, 4),
(107, 'Karan', 55000.00, 4),
(108, 'Pooja', 28000.00, 1),
(109, 'Vijay', 70000.00, 2),
(110, 'Ankit', 32000.00, 5),
(111, 'Meena', 65000.00, 3),
(112, 'Arjun', 25000.00, 5);

SELECT * FROM employee;
SELECT * FROM department;