-- Q1. The HR department wants to display all employees with their respective department names.

-- Write a query using INNER JOIN.

SELECT e.emp_id, e.emp_name, d.dept_name
FROM employee e
INNER JOIN department d
ON e.dept_id = d.dept_id;



-- Q2. The IT department wants to see its employees.

-- Display employee ID, employee name, salary, and department name for employees working in IT.

SELECT e.emp_id, e.emp_name, e.salary, d.dept_name
FROM employee e
INNER JOIN department d
ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';

-- Q3. The company wants to find employees earning more than 50000.

-- Display employee name, salary, and department name.

SELECT e.emp_name, e.salary, d.dept_name
FROM employee e
INNER JOIN department d
ON e.dept_id = d.dept_id
WHERE e.salary > 50000;

-- Q4. The management wants to display all projects along with their department names and budgets.

SELECT p.project_id, p.project_name, d.dept_name, p.budget
FROM project p
INNER JOIN department d
ON p.dept_id = d.dept_id;

-- Q5. Display employees who work in the Finance or Sales department.

SELECT e.emp_name, e.salary, d.dept_name
FROM employee e
INNER JOIN department d
ON e.dept_id = d.dept_id
WHERE d.dept_name="finance" OR d.dept_name="sales";
