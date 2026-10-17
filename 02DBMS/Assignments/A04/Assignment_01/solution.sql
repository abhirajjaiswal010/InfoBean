create database if not exists EmployeeManagementSystem;
use EmployeeManagementSystem;

CREATE TABLE if NOT exists employee(
    employee_id INT primary key auto_increment  ,
    employee_name varchar(50),
    department varchar(20),
    city varchar(20),
    salary decimal(10, 2) check(salary >= 0),
    experience_in_years decimal(4, 1)  default 0.0,
    age INT check(age > 0),
    joining_date DATE,
        CONSTRAINT unique_employee_record
        UNIQUE (employee_name, department, city, joining_date)


);



INSERT ignore INTO employee
    (employee_name, department, city, salary, experience_in_years, age, joining_date)
VALUES
    ('Aarav Sharma',  'IT',      'Indore',   45000.00, 2.5, 24, '2024-01-15'),
    ('Priya Verma',  'HR',      'Bhopal',   35000.00, 3.0, 27, '2023-06-10'),
    ('Rahul Patel',  'FIN',     'Mumbai',   55000.00, 4.5, 29, '2022-11-21'),
    ('Sneha Gupta',  'SAL',     'Pune',     40000.00, 1.5, 23, '2025-02-01'),
    ('Vikram Singh', 'IT',      'Bangalore',95000.00, 8.0, 38, '2020-08-17'),
    ('Ananya Joshi', 'SAL',     'Indore',   32000.00, 1.0, 22, '2026-01-14'),
    ('Rohan Mehta',  'HR',      'Delhi',    42000.00, 3.5, 28, '2022-04-05'),
    ('Kavya Nair',   'IT',      'Bangalore',68000.00, 5.0, 30, '2021-09-20'),
    ('Aditya Mishra','FIN',     'Bhopal',   38000.00, 2.0, 25, '2024-05-13'),
    ('Ishita Jain',  'SAL',     'Pune',     48000.00, 4.0, 29, '2023-12-01');


SELECT * FROM employee;

-- & Question-01 Employees whose salary is greater than ₹60,000.
SELECT "Employees whose salary is greater than ₹60,000." AS Query_01;

SELECT * FROM employee 
WHERE salary>60000;

-- & Question-02 Employees whose salary is less than ₹50,000.
SELECT "Employees whose salary is less than ₹50,000." AS Query_02;

SELECT * FROM employee 
WHERE salary<50000;

-- & Question-03 Employees whose age is greater than 30.
SELECT "Employees whose age is greater than 30." AS Query_03;

SELECT * FROM employee 
WHERE age>30;

-- & Question-04 Employees whose experience is greater than or equal to 5 years.
SELECT "Employees whose experience is greater than or equal to 5 years." AS Query_04;

SELECT * FROM employee 
WHERE experience_in_years >=5;


-- & Question-05 Employees working in IT or Finance.
SELECT "Employees working in IT or Finance." AS Query_05;

SELECT * FROM employee 
WHERE department IN ("it","fin");

-- & Question-06 Employees working in IT, HR, or Sales.
SELECT "Employees working in IT, HR, or Sales." AS Query_06;

SELECT * FROM employee 
WHERE department IN ("it","fin","sal");

-- & Question-07 Employees not working in IT or HR.
SELECT "Employees not working in IT or HR." AS Query_07;

SELECT * FROM employee 
WHERE department NOT IN ("it","hr");


-- & Question-08 Employees from Indore or Pune.
SELECT "Employees from Indore or Pune." AS Query_08;

SELECT * FROM employee 
WHERE city IN ("Indore","Pune");

-- & Question-09 Employees who are not from Indore, Mumbai, or Bhopal.
SELECT "Employees who are not from Indore, Mumbai, or Bhopal." AS Query_09;

SELECT * FROM employee 
WHERE city NOT IN ("Indore","Mumbai","Bhopal");

-- & Question-10 Employees whose salary is between ₹40,000 and ₹70,000.
SELECT "Employees whose salary is between ₹40,000 and ₹70,000." AS Query_10;

SELECT * FROM employee 
WHERE salary BETWEEN 40000 AND 70000; 

-- & Question-11 Employees whose age is between 25 and 35.
SELECT "Employees whose age is between 25 and 35." AS Query_11;

SELECT * FROM employee 
WHERE age BETWEEN 25 AND 35;

-- & Question-12 Employees whose experience is between 3 and 7 years.
SELECT "Employees whose experience is between 3 and 7 years." AS Query_12;

SELECT * FROM employee 
WHERE experience_in_years BETWEEN 3 AND 7;

-- & Question-13 Employees who joined between 2022 and 2025.
SELECT "Employees who joined between 2022 and 2025." AS Query_13;

SELECT * FROM employee 
WHERE Year(joining_date) BETWEEN 2022 AND 2025;

-- & Question-14 Employees who joined before 2023.
SELECT "Employees who joined before 2023." AS Query_14;

SELECT * FROM employee
WHERE year(joining_date)<2023;

-- & Question-15 Employees who joined after 2024.
SELECT "Employees who joined after 2024." AS Query_15;

SELECT * FROM employee
WHERE year(joining_date)>2024;

-- & Question-16 Employees from Indore AND working in IT.
SELECT "Employees from Indore AND working in IT." AS Query_16;

SELECT * FROM employee
WHERE city="indore" AND department="it";

-- & Question-17 Employees working in IT AND having salary greater than ₹70,000.
SELECT "Employees working in IT AND having salary greater than ₹70,000." AS Query_17;

SELECT * FROM employee
WHERE city="indore" AND salary>70000;

-- & Question-18 Employees whose salary is between ₹50,000 and ₹90,000 AND experience is greater than 4 years.
SELECT "Employees whose salary is between ₹50,000 and ₹90,000 AND experience is greater than 4 years." AS Query_18;

SELECT * FROM employee
WHERE salary BETWEEN 50000 AND 90000
 AND experience_in_years>4;

-- & Question-19 Employees working in IT or Finance AND salary greater than ₹60,000.
SELECT "Employees working in IT or Finance AND salary greater than ₹60,000." AS Query_19;

SELECT * FROM employee
WHERE department IN ("it","fin") 
AND salary>60000;

-- -- & Question-20 Employees whose joining date is between 2021 and 2024 AND salary is greater than ₹50,000.
SELECT "Employees whose joining date is between 2021 and 2024 AND salary is greater than ₹50,000." AS Query_20;

SELECT * FROM employee
WHERE year(joining_date) BETWEEN 2021 AND 2024
AND salary>50000;

-- -- & Question-21 Employees whose salary is not between ₹40,000 and ₹70,000.
SELECT "Employees whose salary is not between ₹40,000 and ₹70,000." AS Query_21;

select*FROM employee
WHERE salary NOT BETWEEN 40000 AND 70000;

-- & Question-22 Employees whose department is not IT, HR, or Sales.
SELECT "Employees whose department is not IT, HR, or Sales." AS Query_22;

SELECT*FROM employee
WHERE department NOT IN ("it","hr","sales");

-- & Question-23 Employees whose joining date is not between 2022 and 2025.
SELECT "Employees whose joining date is not between 2022 and 2025." AS Query_23;

SELECT * FROM employee
WHERE year(joining_date) NOT BETWEEN 2022 AND 2025;

-- & Question-24 Employees from Indore or Pune, whose salary is between ₹45,000 and ₹80,000, and whose experience is more than 3 years.
SELECT "Employees from Indore or Pune, whose salary is between ₹45,000 and ₹80,000, and whose experience is more than 3 years." AS Query_24;

SELECT * FROM employee
WHERE city IN ("indore","pune") 
AND salary BETWEEN 45000 AND 80000
AND experience_in_years>3;

-- & Question-25 Employees who did not join between 2020 and 2023 and whose salary is greater than ₹60,000.
SELECT "Employees who did not join between 2020 and 2023 and whose salary is greater than ₹60,000." AS Query_25;

SELECT * FROM employee
WHERE year(joining_date) NOT BETWEEN 2020 AND 2023
AND salary>60000;

-- & Question-26 Employees from Indore, Pune, or Bangalore, whose salary is between ₹50,000 and ₹90,000, and whose experience is at least 4 years.
SELECT "Employees from Indore, Pune, or Bangalore, whose salary is between ₹50,000 and ₹90,000, and whose experience is at least 4 years." AS Query_26;

SELECT * FROM employee
WHERE city IN ("indore","pune","bangalore")
AND salary BETWEEN 50000 AND 90000
AND experience_in_years>=4;

-- & Question-27 Employees who are not from Bhopal or Mumbai, are not working in HR, and joined between 2021 and 2025.
SELECT "Employees who are not from Bhopal or Mumbai, are not working in HR, and joined between 2021 and 2025." AS Query_27;


SELECT * FROM employee
WHERE city NOT IN ("bhopal","mumbai")
AND department<>"hr"
AND year(joining_date) BETWEEN 2021 AND 2025;

-- & Question-28 Employees working in IT or Finance, whose salary is greater than ₹60,000, whose age is between 25 and 35, and who joined after 2022.
SELECT "Employees working in IT or Finance, whose salary is greater than ₹60,000, whose age is between 25 and 35, and who joined after 2022." AS Query_28;

SELECT * FROM employee
WHERE department IN ("it","fin")
AND salary>=60000
AND age BETWEEN 25 AND 35
AND year(joining_date)>2022;

-- & Question-29 Employees whose salary is NOT between ₹40,000 and ₹75,000, whose experience is between 2 and 8 years, and who are not working in Sales.
SELECT "Employees whose salary is NOT between ₹40,000 and ₹75,000, whose experience is between 2 and 8 years, and who are not working in Sales." AS Query_29;

SELECT * FROM employee
WHERE salary NOT BETWEEN 40000 AND 75000
AND experience_in_years BETWEEN 2 AND 8
AND department NOT IN ("sal");

-- & Question-30 Employees from Indore or Pune, working in IT, Finance, or HR, with salary between ₹45,000 and ₹85,000, and who joined between 2020 and 2024.
SELECT "Employees from Indore or Pune, working in IT, Finance, or HR, with salary between ₹45,000 and ₹85,000, and who joined between 2020 and 2024." AS Query_30;

SELECT * FROM employee
where city IN ("indore","pune")
AND department IN ("it","fin","hr")
AND salary BETWEEN 45000 AND 85000
AND year(joining_date) BETWEEN 2020 AND 2024;



DROP DATABASE EmployeeManagementSystem;