
CREATE TABLE IF NOT EXISTS department_pdbc
(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS employee_pdbc
(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(60),
    salary DECIMAL(10,2),
    job_title VARCHAR(50),
    dept_id INT,
    manager_id INT,

    CONSTRAINT fk_employee_department
        FOREIGN KEY (dept_id)
        REFERENCES department_pdbc(dept_id),

    CONSTRAINT fk_employee_employee
        FOREIGN KEY (manager_id)
        REFERENCES employee_pdbc(emp_id)
);
