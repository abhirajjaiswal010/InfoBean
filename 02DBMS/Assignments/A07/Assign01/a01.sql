
CREATE DATABASE IF NOT EXISTS EmployeeDB;
USE EmployeeDB;

DROP TABLE IF EXISTS empTable;

CREATE TABLE IF NOT EXISTS empTable (
    empId INT AUTO_INCREMENT PRIMARY KEY,
    empName VARCHAR(20),
    department ENUM('hr', 'it', 'finance'),
    jobRole ENUM('Manager', 'Recruiter', 'developer', 'tester', 'analyst'),
    salary DECIMAL(10,2),
    hireDate DATE
);

INSERT INTO empTable (empName, department, jobRole, salary, hireDate)
VALUES
('Rahul', 'it', 'developer', 45000, '2021-03-12'),
('Priya', 'hr', 'Recruiter', 32000, '2022-06-20'),
('Amit', 'finance', 'analyst', 55000, '2020-11-05'),
('Neha', 'it', 'tester', 38000, '2023-01-15'),
('Vikram', 'finance', 'Manager', 75000, '2019-08-10'),
('Sneha', 'hr', 'Manager', 62000, '2021-09-25'),
('Karan', 'it', 'developer', 68000, '2020-04-18'),
('Pooja', 'finance', 'analyst', 42000, '2022-12-01'),
('Rohit', 'it', 'tester', 35000, '2024-02-10'),
('Anjali', 'hr', 'Recruiter', 30000, '2023-07-22');

-- SELECT * FROM empTable;

-- Query 01 - Find the total number of employees in each department.
SELECT "Find the total number of employees in each department." AS Query01;


SELECT department, COUNT(*) AS TOTAL_EMP
FROM empTable
GROUP BY department;



-- Query 02 - Find the average salary of employees in each job role.

SELECT "Find the average salary of employees in each job role." AS Query02;

SELECT jobRole,AVG(salary) AS avg_salary
FROM empTable
GROUP BY jobRole;

-- Query 03 - Find the highest salary in the IT department.
SELECT "Find the highest salary in the IT department." AS Query03;

SELECT *
FROM empTable
WHERE department="it"
ORDER BY salary DESC
limit 1;




-- Query 04 - Find the lowest salary among all employees.
SELECT "Find the lowest salary among all employees." AS Query04;

SELECT * 
FROM empTable
ORDER BY salary ASC
limit 1;


-- Query 05 - Count the number of employees who joined after January 1, 2023.
SELECT "Count the number of employees who joined after January 1, 2023" AS Query05;

SELECT count(*) AS noOfEmployees
FROM empTable
WHERE hireDate>="2023-01-01";



-- Query 06 - Find the total salary paid in each department.
SELECT "Find the total salary paid in each department." AS Query06;

SELECT department,sum(salary) AS Total_Salary
FROM empTable
GROUP BY department;


-- Query 07 - Find the job role that has the highest total salary payout.
SELECT "Find the job role that has the highest total salary payout." AS Query07;

SELECT jobRole,sum(salary) AS paid
FROM empTable
GROUP BY jobRole
ORDER BY paid DESC
limit 1;



-- Query 08 - Find the average salary of employees who joined after 2022.

SELECT " Find the average salary of employees who joined after 2022." AS Query08;

SELECT avg(salary) AS avg_salary
FROM empTable
WHERE year(hireDate)>2022;



-- Query 09 - Find departments where the total salary exceeds 10,000.
SELECT " Find departments where the total salary exceeds 10,000." AS Query09;

SELECT department,sum(salary) AS totalSalary
FROM empTable
GROUP BY department
HAVING totalSalary>10000;


-- Query 10 - Find the department with the highest number of employees.
SELECT " Find the department with the highest number of employees." AS Query10;

SELECT department,count(*) AS countEmp
FROM empTable
GROUP BY department
ORDER BY countEmp DESC
limit 1;

