-- QNO 8: Create and Populate Employees Table
-- Columns:
-- emp_id INT
-- emp_name VARCHAR(100)
-- gender VARCHAR(10)
-- dob DATE
-- department VARCHAR(100)
-- position VARCHAR(100)
-- salary DECIMAL(8,2)
-- joining_date DATE
-- phone VARCHAR(15)
-- Task: Insert 5 employee records.
CREATE TABLE
    IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY,
        emp_name VARCHAR(100),
        gender VARCHAR(10),
        dob DATE,
        department VARCHAR(100),
        position VARCHAR(100),
        salary DECIMAL(8, 2),
        joining_date DATE,
        phone VARCHAR(15)
    );

INSERT IGNORE INTO employees (
    emp_id,
    emp_name,
    gender,
    dob,
    department,
    position,
    salary,
    joining_date,
    phone
)
VALUES
    (
        1,
        'Rohit Sharma',
        'Male',
        '1998-05-12',
        'IT',
        'Software Engineer',
        65000.00,
        '2023-07-10',
        '9876500001'
    ),
    (
        2,
        'Priya Verma',
        'Female',
        '1999-08-22',
        'HR',
        'HR Executive',
        42000.00,
        '2024-01-15',
        '9876500002'
    ),
    (
        3,
        'Amit Patel',
        'Male',
        '1997-03-18',
        'Finance',
        'Accountant',
        48000.00,
        '2022-11-01',
        '9876500003'
    ),
    (
        4,
        'Neha Jain',
        'Female',
        '2000-12-05',
        'Marketing',
        'Marketing Executive',
        40000.00,
        '2024-06-20',
        '9876500004'
    ),
    (
        5,
        'Vikram Singh',
        'Male',
        '1996-09-14',
        'IT',
        'Senior Developer',
        85000.00,
        '2021-04-12',
        '9876500005'
    );

SELECT
    *
FROM
    employees;