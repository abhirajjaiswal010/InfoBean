CREATE DATABASE if NOT EXISTS Assign03;
use Assign03;




CREATE TABLE if NOT EXISTS department(
    department_id INT primary key auto_increment,
    department_name varchar(20) unique NOT NULL 
);

CREATE TABLE if NOT EXISTS employee(

    employee_id INT primary key auto_increment,
    employee_name varchar(50) NOT NULL ,
    salary decimal(10,2) NOT NULL,
    department_id INT NOT null,

    constraint fk_employees_department
    foreign key (department_id)
    references  department(department_id)

    on DELETE CASCADE    

);

INSERT IGNORE INTO department(department_name)
values ("CS"),("IT"),("FINANCE");

INSERT ignore into employee(employee_name,salary,department_id)
values
('Rahul', 45000.00, 1),
('Amit', 50000.00, 1),
('Priya', 55000.00, 2),
('Sneha', 60000.00, 2),
('Karan', 40000.00, 3);

-- Display all employees along with their department names without using JOIN.

SELECT
    e.employee_id,
    e.employee_name,
    e.salary,
    d.department_name
FROM employee e,department d
WHERE e.department_id=d.department_id;

-- Update an employee's department.
UPDATE employee
set department_id=3
WHERE employee_id=1;

-- Delete a department and observe what happens to its employees.

DELETE FROM department
WHERE department_id=1;