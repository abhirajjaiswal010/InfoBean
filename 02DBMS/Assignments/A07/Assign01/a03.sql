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


-- Find the total number of employees in each department and display only those departments having more than 2 employees. (GROUP BY + HAVING)

SELECT department,count(*) AS no_of_emp
FROM empTable
GROUP BY department
HAVING no_of_emp>2;



-- Find the total salary paid in each department and display the results in descending order of total salary. (GROUP BY + ORDER BY)


SELECT department,sum(salary) AS Total_Salary
FROM empTable
GROUP BY department
ORDER BY Total_Salary desc;

-- Find the job role that has the highest total salary payout, displaying only roles where total salary is above 10,000. (GROUP BY + HAVING + ORDER BY)

SELECT jobRole,sum(salary) AS Total_Salary
FROM empTable
GROUP BY jobRole
HAVING Total_Salary>10000
ORDER BY Total_Salary desc;


-- Find the average salary of employees who joined after 2022, displaying only job roles where the average salary is above 4500. (WHERE + GROUP BY + HAVING)

SELECT jobrole,avg(salary) AS avg_salary
FROM empTable
WHERE year(hireDate)>2022
GROUP BY jobrole
HAVING avg_salary>4500;

-- Find departments where the total salary exceeds 10,000 and order the results in ascending order of department name. (GROUP BY + HAVING + ORDER BY)

SELECT department,sum(salary) AS Total_Salary
FROM empTable
GROUP BY department
HAVING Total_Salary>10000
ORDER BY department ASC;