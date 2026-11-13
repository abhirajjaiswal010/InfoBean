-- Q6. The HR department wants a complete employee list, including employees who are not assigned to any department.

-- Write a query using LEFT JOIN.

SELECT e.emp_id, e.emp_name, e.salary, d.dept_name
FROM employee e
LEFT JOIN department d
ON e.dept_id = d.dept_id;



-- Q7. Find employees who do not belong to any department.

SELECT e.emp_id, e.emp_name, e.salary, e.dept_id
FROM employee e
LEFT JOIN department d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

-- Q8. The management wants to see all departments with their employees, including departments that have no employees.

SELECT d.dept_id, d.dept_name, e.emp_id, e.emp_name
FROM department d
LEFT JOIN employee e
ON d.dept_id = e.dept_id;

-- Q9. Find the departments that currently have no employees.

SELECT d.dept_id, d.dept_name
FROM department d
LEFT JOIN employee e
ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- Q10. The company wants to display all departments and their projects, including departments that have no projects.

-- Use RIGHT JOIN.

SELECT d.dept_id, d.dept_name, p.project_id, p.project_name, p.budget
FROM project p
RIGHT JOIN department d
ON p.dept_id = d.dept_id;