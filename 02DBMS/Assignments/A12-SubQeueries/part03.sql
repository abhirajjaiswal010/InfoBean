-- Q51. Display employees who work in the department having the lowest average salary.


SELECT *
FROM employee e1
WHERE (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e1.dept_id = e2.dept_id
) = (
    SELECT MIN(avg_salary)
    FROM (
        SELECT dept_id, AVG(salary) AS avg_salary
        FROM employee
        GROUP BY dept_id
    ) AS temp
);


-- Q52. Display departments having more employees than the average number of employees per department.

-- SELECT COUNT(e.emp_id) AS emp_count, d.dept_name
-- FROM employee e, department d
-- WHERE e.dept_id = d.dept_id
-- GROUP BY e.dept_id, d.dept_name;

-- ? avg count of emp as per department

-- SELECT avg(emp_count)
-- FROM (SELECT COUNT(emp_id) AS emp_count
-- FROM employee 
-- GROUP BY dept_id) AS temp


SELECT d.dept_id,d.dept_name,count(e.emp_id) AS emp_count
FROM department d
JOIN employee e
on d.dept_id=e.dept_id
GROUP BY d.dept_id,d.dept_name
HAVING emp_count>(SELECT avg(emp_count)
FROM (SELECT COUNT(emp_id) AS emp_count
FROM employee 
GROUP BY dept_id) AS temp);





-- Q53. Display departments where every employee earns more than 30,000.

SELECT *
FROM department
WHERE dept_id IN (SELECT dept_id
FROM employee
GROUP BY dept_id
HAVING min(salary)>30000);


-- Q54. Display departments where at least one employee earns more than 50,000 and at least one employee earns less than 35,000.

SELECT *
FROM department
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    WHERE salary>50000
    GROUP BY dept_id
) AND dept_id IN (SELECT dept_id
    FROM employee
    WHERE salary<35000
    GROUP BY dept_id);


-- Q55. Display departments where every employee earns less than 70,000.

SELECT *
FROM department
WHERE dept_id in(
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING max(salary)<70000
    
);


-- Q56. Display employees whose salary is greater than the average of all department average salaries.

SELECT e.emp_id,e.emp_name,e.salary,d.dept_name,d.dept_id
FROM employee e 
JOIN department d
on e.dept_id=d.dept_id
WHERE e.salary>
(SELECT AVG(avg_sal)
FROM (
    SELECT AVG(salary) AS avg_sal, dept_id
    FROM employee
    GROUP BY dept_id
) AS temp);


-- Q57. Display the department whose maximum employee salary is the highest among all departments.


-- Q57. Display the department whose maximum employee salary is the highest among all departments.

SELECT d.dept_id, d.dept_name
FROM department d
WHERE d.dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING MAX(salary) = (
        SELECT MAX(max_salary)
        FROM (
            SELECT MAX(salary) AS max_salary
            FROM employee
            GROUP BY dept_id
        ) AS dept_salary
    )
);

-- Q58. Display the department whose minimum employee salary is the lowest among all departments.

SELECT dept_id, dept_name
FROM department
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING MIN(salary) = (
        SELECT MIN(min_salary)
        FROM (
            SELECT MIN(salary) AS min_salary
            FROM employee
            GROUP BY dept_id
        ) AS dept_salary
    )
);

-- Q59. Display employees whose salary is greater than the maximum salary of the HR department.


SELECT *
FROM employee
WHERE salary > (
    SELECT MAX(salary)
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'HR'
    )
);

-- Q60. Display employees whose salary is less than the minimum salary of the Finance department.

SELECT *
FROM employee
WHERE salary < (
    SELECT MIN(salary)
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'Finance'
    )
);

-- Q61. Display employees whose salary is greater than every employee in HR but less than the salary of at least one employee in IT.

SELECT *
FROM employee
WHERE salary>all( 
    SELECT salary
    FROM employee
    WHERE dept_id=(
        SELECT dept_id
        FROM department
        WHERE dept_name="hr"
    )
) AND salary<any(
    
        SELECT salary
        FROM employee
        WHERE dept_id=(
            SELECT dept_id
            FROM department
            WHERE dept_name="it"
        )
    
);


-- Q62. Display employees whose salary is greater than at least one employee in Finance but less than every employee in IT.

SELECT *
FROM employee
WHERE salary>any( 
    SELECT salary
    FROM employee
    WHERE dept_id=(
        SELECT dept_id
        FROM department
        WHERE dept_name="finance"
    )
) AND salary<all(
    
        SELECT salary
        FROM employee
        WHERE dept_id=(
            SELECT dept_id
            FROM department
            WHERE dept_name="it"
        )
    
);


-- Q63. Display employees who work in departments where the department's average salary is greater than 40,000.

-- SELECT avg(salary) AS avg_salary , dept_id
-- FROM employee
-- GROUP BY dept_id
-- HAVING avg_salary>40000;

SELECT * 
FROM employee
WHERE dept_id IN (SELECT dept_id
FROM employee
GROUP BY dept_id
HAVING avg(salary)>40000);

-- Q64. Display departments where the average salary is greater than 40,000 and at least one employee earns more than 60,000.

SELECT *
FROM department
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING avg(salary)>40000
) AND dept_id in  (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING salary>60000

);


-- Q65. Display employees whose salary is greater than their department's average salary but less than the company's overall average salary.

SELECT *
FROM employee e1
WHERE e1.salary>(
    SELECT avg(e2.salary)
    FROM employee e2
    WHERE e1.dept_id=e2.dept_id
) AND e1.salary<(
    SELECT avg(salary)
    FROM employee
);


-- Q66. Display employees whose salary is less than their department's average salary but greater than the company's overall average salary.
SELECT *
FROM employee e1
WHERE e1.salary<(
    SELECT avg(e2.salary)
    FROM employee e2
    WHERE e1.dept_id=e2.dept_id
) AND e1.salary>(
    SELECT avg(salary)
    FROM employee
);



-- Q67. Display the highest-paid employee from each department without using GROUP BY to directly select the employee.

SELECT e1.emp_id,e1.emp_name,e1.salary,d.dept_id,d.dept_name
FROM employee e1
JOIN department d
on e1.dept_id=d.dept_id
WHERE e1.salary=(
    SELECT max(e2.salary)
    FROM employee e2
    WHERE e1.dept_id=e2.dept_id
);

-- Q68. Display the second-highest salary employee from each department.

SELECT e1.emp_id,e1.emp_name,e1.salary ,d.dept_id,d.dept_name
FROM employee e1
JOIN department d
on e1.dept_id=d.dept_id
WHERE e1.salary=(
    SELECT max(e2.salary)
    FROM employee e2
    WHERE e1.dept_id=e2.dept_id
    AND e2.salary<(
        SELECT max(e3.salary)
        FROM employee e3
        WHERE e3.dept_id=e1.dept_id
    )
);

-- Q69. Display departments that have at least two employees.

SELECT *
FROM department
WHERE dept_id IN (

    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING count(emp_id)>=2    
);


-- Q70. Display employees working in departments that have more employees than the HR department.

SELECT *
FROM employee e1
WHERE e1.dept_id IN (

    SELECT e2.dept_id
    FROM employee e2
    GROUP BY e2.dept_id
    HAVING COUNT(*) > (

       SELECT COUNT(*)
FROM employee e3
WHERE e3.dept_id = (
    SELECT dept_id
    FROM department
    WHERE dept_name = 'HR'
)
    )

);


-- Q71. Display employees working in departments that have fewer employees than the IT department.

SELECT *
FROM employee e1
WHERE e1.dept_id IN (

    SELECT e2.dept_id
    FROM employee e2
    GROUP BY e2.dept_id
    HAVING COUNT(*) < (

       SELECT COUNT(*)
FROM employee e3
WHERE e3.dept_id = (
    SELECT dept_id
    FROM department
    WHERE dept_name = 'it'
)
    )

);


-- Q72. Display the department(s) having the same average salary as the Finance department.

SELECT *
FROM department
WHERE dept_id IN (

    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING AVG(salary) = (

        SELECT AVG(salary)
        FROM employee e1
        JOIN department d
        ON e1.dept_id = d.dept_id
        WHERE d.dept_name = 'Finance'

    )

);

-- Q73. Display employees whose salary is equal to the highest salary of any department other than their own department.

SELECT *
FROM employee e1
WHERE e1.salary IN (
    SELECT max(e2.salary)
    FROM employee e2
    WHERE e1.dept_id<>e2.dept_id
    GROUP BY e2.dept_id
);


-- Q74. Display employees whose salary is greater than the average salary of every department.

SELECT *
FROM employee e1
WHERE e1.salary > all (
    SELECT avg(e2.salary)
    FROM employee e2
    GROUP BY e2.dept_id
);


-- Q75. Display employees whose salary is greater than the average salary of at least one department.


SELECT *
FROM employee e1
WHERE e1.salary> any(
    SELECT avg(e2.salary)
    FROM employee e2
    GROUP BY e2.dept_id
);


-- Q76. Display the employee whose salary is closest to the company's average salary.

SELECT *
FROM employee e1
WHERE ABS(
    e1.salary - (
        SELECT avg(salary)
        FROM employee
    )
) = (
    SELECT min(
        abs(e2.salary-(
            SELECT avg(salary)
            FROM employee 

        ))
    ) FROM employee e2
);


-- Q77. Display the department whose average salary is closest to the company's overall average salary.

SELECT *
FROM department d


-- Q78. Display employees who are earning more than the average salary of all employees but are not the highest-paid employee.


-- Q79. Display employees who earn more than the average salary of their department and whose department has at least two employees.


-- Q80. Find employees who satisfy all of the following conditions:
-- Salary is greater than the company average salary.
-- Salary is greater than their department average salary.
-- Their department has at least two employees.
-- They are not the highest-paid employee in the company.