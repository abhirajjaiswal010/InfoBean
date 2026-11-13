-- Q1. Display all employees whose salary is greater than the average salary of all employees.

SELECT * FROM employee
WHERE salary>(
    SELECT avg(salary)
    FROM employee
);

-- Q2. Display the employee or employees who receive the highest salary in the company.

SELECT * FROM employee
WHERE salary=(
    SELECT max(salary)
    FROM employee

);

-- Q3. Display the employee or employees who receive the lowest salary in the company.

SELECT * FROM employee
WHERE salary=(
    SELECT min(salary)
    FROM employee

);

-- Q4. Display all employees whose salary is greater than the salary of Amit.

SELECT * FROM employee
WHERE salary>(
    SELECT salary
    FROM employee
    WHERE emp_id=112

);

-- Q5. Display all employees whose salary is less than the salary of Rahul.

SELECT * FROM employee
WHERE salary<(
    SELECT salary
    FROM employee
    WHERE emp_id=102

);


-- Q6. Display employees who work in departments located in Indore.
-- Expected columns: emp_id, emp_name, salary, dept_id

SELECT * FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE location="Indore"
);

-- Q7. Display employees who work in the IT or Finance departments. Obtain the department IDs using a subquery (do not hardcode values such as 2, 3).

SELECT * FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE dept_name IN ("it","finance")
);


-- Q8. Display employees who do not work in departments located in Indore.

SELECT * FROM employee
WHERE dept_id NOT IN (
    SELECT dept_id
    FROM department
    WHERE location="Indore"
);

-- Q9. Display departments that currently have no employees.

SELECT * FROM department
WHERE dept_id NOT IN (SELECT dept_id FROM employee);


-- Q10. Display employees whose salary is greater than the average salary of the IT department.

SELECT * FROM employee
WHERE salary>(
    SELECT avg(salary)
    FROM employee
    WHERE dept_id IN (
        SELECT dept_id
        FROM department
        WHERE dept_name="it"
    )
);

-- Q11. Display employees whose salary is greater than the average salary of the Finance department.

SELECT * FROM employee
WHERE salary>(
    SELECT avg(salary)
    FROM employee
    WHERE dept_id IN (
        SELECT dept_id
        FROM department
        WHERE dept_name="finance"
    )
);


-- Q12. Display employees whose salary is equal to the highest salary in the IT department.

SELECT * FROM employee
WHERE salary=(
    SELECT max(salary)
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name="it"
    )
);

-- Q13. Display employees whose salary is less than the lowest salary in the Sales department.

SELECT * FROM employee
WHERE salary<(
    SELECT min(salary)
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name="sales"
    )
);

-- Salary greater than ANY means greater than at least one HR salary.



-- Salary greater than ALL means greater than every HR salary.

-- Q14. Display employees whose salary is greater than at least one employee working in the HR department.

SELECT * FROM employee
WHERE salary> ANY(
    SELECT salary
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name="hr"
    )
);


-- Q15. Display employees whose salary is greater than every employee working in the HR department.

SELECT * FROM employee
WHERE salary> All(
    SELECT salary
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name="hr"
    )
);


-- Q16. Display employees whose salary is less than at least one employee working in the IT department.

SELECT * FROM employee
WHERE salary< any(
    SELECT salary
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name="it"
    )
);


-- Q17. Display employees whose salary is greater than every employee working in the Finance department.


SELECT * FROM employee
WHERE salary> all(
    SELECT salary
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name="finance"
    )
);


-- Q18. Display employees whose salary is below the salary of every employee working in the IT department.

SELECT * FROM employee
WHERE salary< all(
    SELECT salary
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name="it"
    )
);


-- ? correlated subquereis -> depend on outside queries
-- Q19. Display employees whose salary is greater than their own department's average salary.

SELECT * 
FROM employee e1
WHERE salary>(
    SELECT avg(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);

-- Q20. Display employees whose salary is less than their own department's average salary.

SELECT * 
FROM employee e1
WHERE salary<(
    SELECT avg(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);



-- Q21. Display employees whose salary is exactly equal to their own department's average salary.

SELECT * 
FROM employee e1
WHERE salary=(
    SELECT avg(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);



-- Q22. Display the employee or employees who receive the highest salary in each department.
-- Expected columns: emp_id, emp_name, salary, dept_id

SELECT * 
FROM employee e1
WHERE salary=(
    SELECT max(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);

-- Q23. Display the employee or employees who receive the lowest salary in each department.

SELECT * 
FROM employee e1
WHERE salary=(
    SELECT min(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);

-- Q24. Display employees who are not the highest-paid employees of their respective departments.

SELECT * 
FROM employee e1
WHERE salary<(
    SELECT max(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);


-- Q25. Display employees who are not the lowest-paid employees of their respective departments.

SELECT * 
FROM employee e1
WHERE salary>(
    SELECT min(e2.salary)
    FROM employee e2
    WHERE e2.dept_id=e1.dept_id
);