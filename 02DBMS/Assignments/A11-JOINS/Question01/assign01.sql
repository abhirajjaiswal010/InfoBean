-- Write an SQL query to display employee IDs, employee names, and their corresponding department names using INNER JOIN.

SELECT e.emp_id,e.emp_name,d.dept_name
FROM employee e 
INNER JOIN department d
on e.dept_id=d.dept_id;





-- Modify the query to display only employees who belong to the HR department.

SELECT e.emp_id,e.emp_name,d.dept_name
FROM Employee e
INNER JOIN department d
on e.dept_id=d.dept_id
WHERE d.dept_name="hr";