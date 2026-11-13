-- Q13. The company wants to display each employee's name along with their manager's name.
-- Use SELF JOIN.


SELECT 
    e.emp_name AS employee_name,
    m.emp_name AS manager_name
FROM employee e
JOIN employee m
    ON e.manager_id = m.emp_id;




-- Q14. Find employees who do not have any manager.


SELECT 
    e.emp_name AS employee_name,
    m.emp_name AS manager_name
FROM employee e
LEFT JOIN employee m
    ON e.manager_id = m.emp_id
WHERE e.manager_id IS null;

SELECT * FROM employee;

-- Q15. The management wants to find employees whose salary is greater than their manager's salary.
-- Display employee name, employee salary, manager name, and manager salary.

SELECT 
    e.emp_name AS employee_name,
    e.salary AS employee_salary,
    m.emp_name AS manager_name,
    m.salary AS manager_salary
FROM employee e
JOIN employee m
    ON e.manager_id = m.emp_id
WHERE e.salary>m.salary;

-- Q16. Find employees who report to the same manager.
-- Display both employee names and their manager's name.    

SELECT 
    e1.emp_name AS employee1,
    e2.emp_name AS employee2,
    m.emp_name AS manager_name
FROM employee e1
JOIN employee e2
   on e1.manager_id=e2.manager_id
JOIN employee m
   on e1.manager_id=m.emp_id
WHERE e1.emp_id<e2.emp_id;

-- e1.emp_id < e2.emp_id duplicate pairs avoid karta hai.

