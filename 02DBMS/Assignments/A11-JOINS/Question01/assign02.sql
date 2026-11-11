-- Problem Statement

-- Using the same Employees and Departments tables from Assignment 1, perform the following tasks.

-- Tasks

-- Write an SQL query using LEFT JOIN to display all employees along with their department names, including employees who do not belong to any department.
SELECT e.emp_id,e.emp_name,d.dept_name
FROM employee e
LEFT JOIN department d
on e.dept_id=d.dept_id;


-- Write an SQL query to count the number of employees who do not belong to any department.

SELECT count(e.emp_id) AS total_emp
FROM employee e
LEFT JOIN department d
on e.dept_id=d.dept_id
WHERE d.dept_id IS NULL;