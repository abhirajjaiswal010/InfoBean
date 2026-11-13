-- Q17. The project manager wants a report containing employee names, project names, and working hours.

-- Use the employee, employee_project, and project tables.

SELECT
    e.emp_name AS employee_name,
    p.project_name AS Project_name,
    ep.hours_worked AS working_hours
FROM employee e
JOIN employee_project ep
on e.emp_id=ep.emp_id
JOIN project p
on ep.project_id=p.project_id;



-- Q18. Display project names along with their department names and budgets.

SELECT
    p.project_name AS project_name,
    d.dept_name AS department_name,
    p.budget AS budgets
FROM project p
JOIN department d
on p.dept_id=d.dept_id;


-- Q19. The company wants a complete employee project report.
-- Display employee name, department name, project name, and working hours.

SELECT 
    e.emp_name employee_name,
    d.dept_name department_name,
    p.project_name Project_name,
    ep.hours_worked working_hours
FROM employee e
JOIN department d
on e.dept_id=d.dept_id
JOIN employee_project ep
on e.emp_id=ep.emp_id
JOIN project p
on ep.project_id=p.project_id;



-- Q20. Find employees working on projects having a budget greater than 300000.

-- Display employee name, project name, and project budget.


SELECT
    e.emp_name AS employee_name,
    p.project_name AS project_name,   
    p.budget AS budgets
FROM employee e
JOIN employee_project ep
on ep.emp_id=e.emp_id
JOIN project p
on p.project_id=ep.project_id
WHERE p.budget>300000;
