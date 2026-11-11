-- Problem Statement

-- Using the same Employees and Departments tables from Assignment 1, perform the following tasks.

-- Tasks

-- Write an SQL query using RIGHT JOIN to display all departments along with their employees, including departments that have no employees assigned.

SELECT e.emp_id,e.emp_name,d.dept_name
FROM employee e
RIGHT JOIN department d
on e.dept_id=d.dept_id
ORDER BY e.emp_id ASC;


-- Write an SQL query to find the names of departments that have no employees assigned.


SELECT e.emp_id,e.emp_name,d.dept_name
FROM employee e
RIGHT JOIN department d
on e.dept_id=d.dept_id
WHERE e.dept_id IS  NULL;
