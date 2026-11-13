-- Q26. Find employees who are working on more than one project.
-- Display employee name and total project count.

SELECT
    e.emp_name AS employee_name,
    COUNT(ep.project_id) AS total_projects
FROM employee e
JOIN employee_project ep
    ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING COUNT(ep.project_id) > 1;

-- Q27. Find employees who are not assigned to any project but belong to a department.

SELECT e.emp_name,d.dept_name
FROM employee e
JOIN department d
on e.dept_id=d.dept_id
LEFT JOIN employee_project ep
on e.emp_id=ep.emp_id
WHERE ep.emp_id IS null;




-- Q28. CROSS JOIN

-- The company wants to generate all possible employee and project combinations, whether an employee is actually working on that project or not.

-- Write a query using CROSS JOIN.

SELECT
    e.emp_name AS employee_name,
    p.project_name AS project_name
FROM employee e
CROSS JOIN project p;


-- Q29. Find the highest-paid employee in each department.

-- Display employee name, department name, and salary.



SELECT
    e.emp_name AS employee_name,
    d.dept_name AS department_name,
    e.salary
FROM employee e
JOIN department d
    ON e.dept_id = d.dept_id
WHERE e.salary=(
    SELECT max(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);

-- Q30. The management wants to generate a complete department report containing:

-- Department Name
-- Total Employees
-- Total Projects
-- Total Project Budget
-- Total Working Hours
-- Include all departments, even if they have no employees or projects.

-- Make sure that duplicate rows created by multiple JOINs do not affect the aggregate results.