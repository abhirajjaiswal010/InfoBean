
CREATE DATABASE IF NOT EXISTS a06;
USE a06;

DROP TABLE IF EXISTS employee;

CREATE TABLE IF NOT EXISTS employee (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    department VARCHAR(30) NOT NULL,
    designation VARCHAR(30) NOT NULL,
    age INT NOT NULL CHECK (age BETWEEN 21 AND 60),
    salary DECIMAL(10,2) NOT NULL CHECK (salary > 15000),
    experience INT NOT NULL CHECK (experience BETWEEN 0 AND 35),
    joining_year INT NOT NULL,
    status ENUM('Active', 'Inactive', 'OnLeave') NOT NULL,
    bonus DECIMAL(10,2) NOT NULL CHECK (bonus >= 0),

    CONSTRAINT check_age
        CHECK (experience <= age - 21),

    CONSTRAINT check_salary
        CHECK (experience < 10 OR salary >= 50000),

    CONSTRAINT check_dept
        CHECK (
            (department = 'IT'
                AND designation IN ('Developer', 'Tester', 'Team Lead'))
            OR
            (department = 'HR'
                AND designation IN ('HR Executive', 'HR Manager'))
            OR
            (department = 'Finance'
                AND designation IN ('Accountant', 'Finance Manager'))
            OR
            (department = 'Sales'
                AND designation IN ('Sales Executive', 'Sales Manager'))
        ),

    CONSTRAINT check_status_bonus
        CHECK (
            status = 'Active'
            OR (status = 'Inactive' AND bonus = 0)
            OR (status = 'OnLeave' AND bonus <= salary * 0.20)
        ),

    CONSTRAINT check_exp
        CHECK (
            experience <= 2026 - joining_year
            AND joining_year <= 2026
        )
);

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Abhiraj', 'abhiraj@example.com', '9000000001',
 'IT', 'Developer', 25, 35000, 4, 2022, 'Active', 5000),

('Rahul', 'rahul@example.com', '9000000002',
 'IT', 'Tester', 30, 55000, 9, 2017, 'Active', 8000),

('Priya', 'priya@example.com', '9000000003',
 'IT', 'Team Lead', 40, 80000, 15, 2011, 'Active', 15000),

('Aman', 'aman@example.com', '9000000004',
 'HR', 'HR Executive', 24, 28000, 3, 2023, 'Inactive', 0),

('Neha', 'neha@example.com', '9000000005',
 'HR', 'HR Manager', 35, 60000, 10, 2016, 'Active', 10000),

('Vikas', 'vikas@example.com', '9000000006',
 'Finance', 'Accountant', 28, 40000, 6, 2020, 'OnLeave', 8000),

('Sneha', 'sneha@example.com', '9000000007',
 'Finance', 'Finance Manager', 42, 90000, 20, 2006, 'Active', 20000),

('Karan', 'karan@example.com', '9000000008',
 'Sales', 'Sales Executive', 26, 32000, 4, 2022, 'Inactive', 0),

('Pooja', 'pooja@example.com', '9000000009',
 'Sales', 'Sales Manager', 38, 70000, 12, 2014, 'OnLeave', 14000),

('Mohit', 'mohit@example.com', '9000000010',
 'IT', 'Developer', 32, 50000, 8, 2018, 'Active', 7000);


-- ?  not null testing

-- (null, 'karan@example.com', '9000000008',
--  'Sales', 'Sales Executive', 26, 32000, 4, 2022, 'Inactive', 0),

-- ('Pooja', null, '9000000009',
--  'Sales', 'Sales Manager', 38, 70000, 12, 2014, 'OnLeave', 14000),

-- ('Mohit', 'mohit@example.com', '9000000010',
--  'IT', 'Developer', 32, null, 8, 2018, 'Active', 7000);

-- ? unique testing
-- ('Pooja', 'mohit@example.com', '9000000009',
--  'Sales', 'Sales Manager', 38, 70000, 12, 2014, 'OnLeave', 14000),

-- ('Mohit', 'mohit@example.com', '9000000009',
--  'IT', 'Developer', 32, null, 8, 2018, 'Active', 7000);

-- ? indivdual check testing 

-- Test 6: Age equal to 18

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test6', 'test6@example.com', '9110000006',
 'IT', 'Developer', 18, 30000, 0, 2026, 'Active', 1000);


-- Test 7: Salary equal to 10000

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test7', 'test7@example.com', '9110000007',
 'IT', 'Developer', 25, 10000, 4, 2022, 'Active', 1000);

-- Test 8 : Try inserting an employee with experience equal to -2.

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test8', 'test8@example.com', '9110000008',
 'IT', 'Developer', 25, 10000, -4, 2022, 'Active', 1000);


-- Test 9 : Try inserting an employee with bonus equal to -500.

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test9', 'test9@example.com', '9110000009',
 'IT', 'Developer', 25, 10000, -4, 2022, 'Active', -500);

-- Test 10 : Try inserting an employee with status equal to Retired.

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test10', 'test10@example.com', '9110000010',
 'IT', 'Developer', 25, 30000, 4, 2022, 'Retired', 1000);

-- ? combination CHECK testing COMMENT

-- Test 11: Age 25 and Experience 10
INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test11', 'test11@example.com', '9110000011',
 'IT', 'Developer', 25, 60000, 10, 2016, 'Active', 5000);

-- Test 12: experience 12 and salary 35000

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test11', 'test11@example.com', '9110000011',
 'IT', 'Developer', 25, 35000, 12, 2016, 'Active', 5000);

-- Test 13: department IT  and designation HR Mamager

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test11', 'test11@example.com', '9110000011',
 'IT', 'HR Manager', 25, 35000, 12, 2016, 'Active', 5000);


-- Test 14 : status inactive and bonus 5000
INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test12', 'test12@example.com', '9110000012',
 'IT', 'HR Manager ', 25, 35000, 12, 2016, 'InActive', 5000);

-- Test 15: OnLeave Status, Salary 50000, Bonus 15000

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test15', 'test15@example.com', '9110000015',
 'IT', 'Developer', 30, 50000, 8, 2020, 'OnLeave', 15000);

-- Test 16: Joining Year 2020 and Experience 10

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test16', 'test16@example.com', '9110000016',
 'IT', 'Developer', 35, 60000, 10, 2020, 'Active', 5000);

-- Test 17 : Joining Year 2027

INSERT INTO employee
(emp_name, email, phone, department, designation,
 age, salary, experience, joining_year, status, bonus)
VALUES
('Test17', 'test17@example.com', '9110000017',
 'IT', 'Developer', 30, 40000, 5, 2027, 'Active', 5000);
