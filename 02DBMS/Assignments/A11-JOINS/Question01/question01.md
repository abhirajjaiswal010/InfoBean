# SQL Joins Assignment

### Dataset Overview

#### Table 1: Employees

| emp_id | emp_name | dept_id |
| --- | --- | --- |
| 1 | Alice | 101 |
| 2 | Bob | 102 |
| 3 | Charlie | 103 |
| 4 | David | 101 |

#### Table 2: Departments

| dept_id | dept_name |
| --- | --- |
| 101 | HR |
| 102 | IT |
| 104 | Finance |

---

### Assignment 1: Understanding INNER JOIN

#### Problem Statement

Consider the `Employees` and `Departments` tables provided above.

#### Tasks

1. Write an SQL query to display employee IDs, employee names, and their corresponding department names using `INNER JOIN`.
2. Modify the query to display only employees who belong to the HR department.

---

### Assignment 2: LEFT JOIN Practice

#### Problem Statement

Using the same `Employees` and `Departments` tables from Assignment 1, perform the following tasks.

#### Tasks

1. Write an SQL query using `LEFT JOIN` to display all employees along with their department names, including employees who do not belong to any department.
2. Write an SQL query to count the number of employees who do not belong to any department.

---

### Assignment 3: RIGHT JOIN Practice

#### Problem Statement

Using the same `Employees` and `Departments` tables from Assignment 1, perform the following tasks.

#### Tasks

1. Write an SQL query using `RIGHT JOIN` to display all departments along with their employees, including departments that have no employees assigned.
2. Write an SQL query to find the names of departments that have no employees assigned.

---

### Assignment 4: FULL OUTER JOIN Simulation

#### Problem Statement

MySQL does not directly support `FULL OUTER JOIN`. However, its functionality can be simulated using a combination of `LEFT JOIN` and `RIGHT JOIN` with `UNION`.

#### Tasks

1. Write an SQL query to simulate `FULL OUTER JOIN` using `LEFT JOIN` and `RIGHT JOIN`.
2. Display all employees and their corresponding departments.
3. Ensure that unmatched records from both tables are also included in the result.