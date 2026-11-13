-- Q21. Find the total number of employees in each department, including departments having zero employees.

SELECT d.dept_name department_name,
count(e.emp_id) employee_count
FROM department d
LEFT JOIN employee e
on d.dept_id=e.dept_id
GROUP BY d.dept_id,d.dept_name;



-- Q22. Find the average salary of employees in each department.
-- Display department name and average salary.
SELECT d.dept_name department_name,
avg(e.salary) avg_salary
FROM department d
LEFT JOIN employee e
on d.dept_id=e.dept_id
GROUP BY d.dept_name;

-- Q23. Find the total number of employees working on each project, including projects having zero employees.

SELECT
p.project_name ,
count(ep.emp_id) employee_count
FROM project p
LEFT JOIN employee_project ep
on ep.project_id=p.project_id
GROUP BY p.project_name;


-- Q24. The management wants to know the total working hours of each project.

-- Display project name and total working hours.

SELECT
    p.project_name AS project_name,
    SUM(ep.hours_worked) AS total_working_hours
FROM project p
JOIN employee_project ep
    ON p.project_id = ep.project_id
GROUP BY p.project_id, p.project_name;


-- Q25. Find departments having more than two employees.

-- Display department name and employee count.

SELECT 
d.dept_name department_name,
count(e.emp_id) employee_count
FROM department d
LEFT JOIN employee e
on e.dept_id=d.dept_id
GROUP BY d.dept_name
HAVING employee_count>2;