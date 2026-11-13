-- MySQL does not directly support FULL OUTER JOIN.

-- Q11. The management wants a complete report of all employees and departments.
-- Display all employees and all departments, including unmatched records.
-- Use LEFT JOIN, RIGHT JOIN, and UNION.

SELECT e.emp_id, e.emp_name, e.salary, d.dept_id, d.dept_name
FROM employee e
LEFT JOIN department d
ON e.dept_id = d.dept_id

UNION

SELECT e.emp_id, e.emp_name, e.salary, d.dept_id, d.dept_name
FROM employee e
RIGHT JOIN department d
ON e.dept_id = d.dept_id;

-- Q12. Find employees without departments and departments without employees in a single result.

-- Use FULL OUTER JOIN simulation.

SELECT e.emp_id, e.emp_name, d.dept_id, d.dept_name
FROM employee e
LEFT JOIN department d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL

UNION

SELECT e.emp_id, e.emp_name, d.dept_id, d.dept_name
FROM employee e
RIGHT JOIN department d
ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL;