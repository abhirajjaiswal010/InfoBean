-- Q26. Display the second-highest salary in the company without using LIMIT.

SELECT max(salary)
FROM employee
WHERE salary<(
    SELECT max(salary)
    FROM employee
);


-- Q27. Display the employee or employees having the second-highest salary without using LIMIT.

SELECT * 
FROM employee
WHERE salary=(
    SELECT max(salary)
    FROM employee
    WHERE salary<(
        SELECT max(salary)
        FROM employee
    )
);


-- Q28. Display the third-highest salary in the company without using LIMIT.


SELECT max(salary)
FROM employee
WHERE salary<(
    SELECT max(salary)
    FROM employee
    WHERE salary<(
        SELECT max(salary)
        FROM employee
    )
);

-- Q29. Display the employee or employees having the third-highest salary.
SELECT *
FROM employee
WHERE salary=(
    SELECT max(salary)
    FROM employee
    WHERE salary<(
        SELECT max(salary)
        FROM employee
        WHERE salary<(
            SELECT max(salary)
            FROM employee
        )
)

)
-- Q30. Display all departments for which at least one employee exists.

SELECT *
FROM department
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
);

-- Q31. Display all departments for which no employee exists.

SELECT * 
FROM department d
LEFT JOIN employee e
on  d.dept_id=e.dept_id
WHERE e.emp_id IS null;


SELECT *
FROM department d
WHERE d.dept_id NOT IN (
    SELECT dept_id
    FROM employee
    WHERE dept_id IS NOT null
);



-- Q32. Display departments where at least one employee earns more than 60,000.

SELECT *
FROM department d
WHERE d.dept_id IN (
    SELECT dept_id FROM employee 
    WHERE salary>60000
);



-- Q33. Display departments where no employee earns more than 60,000.

SELECT *
FROM department d
WHERE d.dept_id NOT IN (
    SELECT dept_id FROM employee 
    WHERE salary>60000
);



-- Q34. Display departments where at least one employee earns less than 30,000.

SELECT *
FROM department d
WHERE d.dept_id  IN (
    SELECT dept_id FROM employee 
    WHERE salary<30000
);

-- Q35. Display departments where no employee earns less than 30,000.

SELECT * 
FROM department d
WHERE d.dept_id NOT IN (
    SELECT dept_id FROM employee
    WHERE salary<30000
);

-- Q36. Display employees who belong to a department that exists in the department table.

SELECT *
FROM employee e
WHERE e.dept_id  IN (
    SELECT dept_id FROM department 
);

-- Q37. Display employees whose salary is greater than their own department's average salary using a correlated subquery.


SELECT * 
FROM employee e1
WHERE e1.salary>(
    SELECT avg(salary)
    FROM employee e2
    WHERE e1.dept_id=e2.dept_id

);

-- Q38. Display employees whose salary is the maximum salary of their department using a correlated subquery.

SELECT * 
FROM employee e1
WHERE e1.salary=(
    SELECT max(salary)
    FROM employee e2
    WHERE e1.dept_id=e2.dept_id

);

-- Q39. Display employees whose salary is the minimum salary of their department using a correlated subquery.

SELECT * 
FROM employee e1
WHERE e1.salary=(
    SELECT min(salary)
    FROM employee e2
    WHERE e1.dept_id=e2.dept_id

);

-- Q40. Display each employee along with the average salary of their department.
-- Expected columns: emp_id, emp_name, salary, dept_id, department_average_salary

SELECT e1.emp_id,
       e1.emp_name,
       e1.salary,
       e1.dept_id,
        (SELECT avg(e2.salary)
        FROM employee e2
        WHERE e2.dept_id=e1.dept_id)
AS department_average_salary
FROM employee e1;


-- Q41. Display each employee along with the highest salary in their department.
-- Expected columns: emp_id, emp_name, salary, dept_id, department_highest_salary

SELECT e1.emp_id,
       e1.emp_name,
       e1.salary,
       e1.dept_id,
        (SELECT max(e2.salary)
        FROM employee e2
        WHERE e2.dept_id=e1.dept_id)
AS department_max_salary
FROM employee e1;

-- Q42. Display each employee along with the lowest salary in their department.
-- Expected columns: emp_id, emp_name, salary, dept_id, department_lowest_salary

SELECT e1.emp_id,
       e1.emp_name,
       e1.salary,
       e1.dept_id,
        (SELECT min(e2.salary)
        FROM employee e2
        WHERE e2.dept_id=e1.dept_id)
AS department_min_salary
FROM employee e1;


-- Q43. Display each employee along with the company's overall average salary.
-- Expected columns: emp_id, emp_name, salary, company_average_salary

SELECT e1.emp_id,
       e1.emp_name,
       e1.salary,
       (
           SELECT AVG(e2.salary)
           FROM employee e2
       ) AS company_average_salary
FROM employee e1;


-- Q44. Display each employee along with the difference between their salary and the company's average salary.
-- Expected columns: emp_id, emp_name, salary, salary_difference


SELECT e1.emp_id,
       e1.emp_name,
       e1.salary,
       (e1.salary-(
           SELECT AVG(e2.salary)
           FROM employee e2
       ) )
       AS salary_difference
FROM employee e1;


-- Q45. Display each employee along with the name of their department, obtaining the department name via a subquery.
-- Expected columns: emp_id, emp_name, salary, dept_name
SELECT e1.emp_id,
       e1.emp_name,
       e1.salary,
       (SELECT d.dept_name
       FROM department d
       WHERE d.dept_id=e1.dept_id) AS dept_name
       
FROM employee e1 ;


-- Q46. Display departments whose average salary is greater than the average salary of the entire company.

SELECT *
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) > (
    SELECT AVG(salary)
    FROM employee
);


-- Q47. Display departments whose average salary is less than the average salary of the entire company.

SELECT *
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) < (
    SELECT AVG(salary)
    FROM employee
);


-- Q48. Display the department having the highest average salary.

SELECT *
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT max(salary)
    FROM employee
);
-- Q49. Display the department having the lowest average salary.

SELECT *
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) < (
    SELECT min(salary)
    FROM employee
);

--? Q50. Display employees who work in the department having the highest average salary.

-- Description:

-- Find the average salary of each department and identify the department with the highest average salary. Then display all employees who belong to that department.

-- Concepts Used:
-- Correlated Subquery
-- Nested Subquery
-- Derived Table
-- Aggregate Functions (AVG, MAX)
-- GROUP BY

-- SELECT max(avg_salary)
-- FROM (SELECT dept_id,avg(salary) AS avg_salary
--     FROM employee 
--     GROUP BY dept_id) AS temp;

SELECT *
FROM employee e1
WHERE (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e1.dept_id = e2.dept_id
) = (
    SELECT MAX(avg_salary)
    FROM (
        SELECT dept_id, AVG(salary) AS avg_salary
        FROM employee
        GROUP BY dept_id
    ) AS temp
);

