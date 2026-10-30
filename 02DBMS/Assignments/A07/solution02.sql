CREATE DATABASE if NOT EXISTS staffDb;
use staffDb;

DROP TABLE if exists staff_table;

CREATE TABLE if NOT exists staff_table(

    staff_id INT primary key auto_increment,
    staff_name varchar(50),
    department varchar(30),
    city varchar(30),
    salary decimal(10,2),
    experience int,
    age int,
    joining_date Date,
    status varchar(20)
);

INSERT into staff_table
(staff_name,department,city,salary,experience,age,joining_date,status)
values
('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),
('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),
('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),
('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),
('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),
('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active'),
('Gaurav', 'Finance', 'Mumbai', 74000, 8, 40, '2017-09-12', 'Active'),
('Heena', 'IT', 'Delhi', 59000, 5, 30, '2020-02-17', 'Inactive'),
('Ishaan', 'Sales', 'Pune', 45000, 2, 25, '2023-01-10', 'Active'),
('Jaya', 'HR', 'Indore', 72000, 7, 36, '2018-07-22', 'Active');


-- Q1. Delete the employee whose name is Aarav using his staff_id.

DELETE FROM staff_table
WHERE staff_id=1;


-- Q2. Delete all employees who belong to the Sales department.

DELETE FROM staff_table
WHERE department="sales";



-- Q3. Delete all employees whose salary is below ₹50,000.

DELETE FROM staff_table
WHERE salary>50000;


-- Q4. Delete all employees who belong to HR and have at least 5 years of experience.

DELETE FROM staff_table
WHERE department="hr"
AND experience>=5;



-- Q5. Delete all employees who are from Indore or Bhopal.

DELETE FROM staff_table
WHERE city IN ("indore","bhopal");

-- Q6. Delete all employees who belong to neither IT nor Finance.

DELETE FROM staff_table
WHERE department NOT IN ("it","finance");


-- Q7. Delete all employees whose salary is between ₹50,000 and ₹65,000, inclusive.

DELETE FROM staff_table
WHERE salary BETWEEN 50000 AND 65000;

-- Q8. Delete all employees who have less than 5 years of experience and whose status is Inactive.

DELETE FROM staff_table
WHERE experience<5 AND status="inactive";

-- Q9. Delete all employees whose names start with the letter D.

DELETE FROM staff_table
WHERE staff_name LIKE "d%";

-- Q10. Delete all employees whose city is NULL.


DELETE FROM staff_table
WHERE city IS NULL;

-- Q11. Delete all employees who joined before January 1, 2020, and have a salary of at least ₹60,000.

DELETE FROM staff_table
WHERE joining_date>"2020-01-01"
AND salary>=60000;

-- Q12. Delete all employees who belong to IT or HR, have at least 3 years of experience, and earn less than ₹70,000.

DELETE FROM staff_table
WHERE department IN ("it","hr")
AND experience>=3
AND salary<=70000;

-- Q13. Delete all employees who are not from Sales, have a salary above ₹55,000, and are currently Active.

DELETE FROM staff_table
WHERE department<> "sales"
AND salary>55000
AND status="active";

-- Q14. Delete all employees who belong to Finance or HR and have a salary below ₹65,000.


DELETE FROM staff_table
WHERE department IN ("finance","hr")
AND salary<65000;

-- Q15. Delete the employee with the lowest salary from the table. If multiple employees have the same lowest salary, delete only one employee.

DELETE FROM staff_name
ORDER BY salary asc
limit 1;


-- Q16. Delete the employee with the highest salary from the table. If multiple employees have the same highest salary, delete only one employee.

DELETE FROM staff_table
ORDER BY salary desc
limit 1;

-- Q17. Delete only the lowest-paid employee who belongs to IT or HR, has at least 3 years of experience, and earns less than ₹70,000.

DELETE FROM staff_table 
WHERE department IN ("it","hr")
AND experience>=3 
AND salary<70000
ORDER BY salary asc
limit 1;


-- Q18. Delete only the highest-paid Active employee having at least 5 years of experience.

DELETE FROM staff_table 
WHERE status="active" AND experience>=5
ORDER BY salary desc
limit 1;


-- Q19. Delete only the lowest-paid employee who is neither from HR nor Sales, has at least 3 years of experience, and earns below ₹70,000.

DELETE FROM staff_table
WHERE department NOT IN ("hr","sales")
AND experience>=3
AND salary<70000
ORDER BY salary asc
limit 1;


-- Q20. Delete all employees who satisfy either of the following conditions:

-- IT employees having at least 5 years of experience and a salary below ₹80,000.
-- Finance employees having a salary below ₹65,000.

DELETE FROM staff_table
WHERE (department="it" AND experience>=5 AND salary<80000)
or
(department="finance" AND salary<65000);