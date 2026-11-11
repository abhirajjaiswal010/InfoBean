-- Problem Statement

-- MySQL does not directly support FULL OUTER JOIN. However, its functionality can be simulated using a combination of LEFT JOIN and RIGHT JOIN with UNION.

-- Tasks

-- Assignment 4: FULL OUTER JOIN Simulation

SELECT
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employee e
LEFT JOIN department d
ON e.dept_id = d.dept_id

UNION

SELECT
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employee e
RIGHT JOIN department d
ON e.dept_id = d.dept_id;