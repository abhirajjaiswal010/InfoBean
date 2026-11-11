# MySQL Subquery Assignment: Employee Management System

## Case Study Overview

**ABC Technologies** is developing an Employee Management System to perform detailed salary, departmental, and workforce analytics using MySQL subqueries.

---

## Database Schema & Sample Data

### Table 1: `department`

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `dept_id` | `INT` | Department ID |
| `dept_name` | `VARCHAR(30)` | Department Name |
| `location` | `VARCHAR(30)` | Department Location |

#### Data

| dept_id | dept_name | location |
| :--- | :--- | :--- |
| 1 | HR | Indore |
| 2 | IT | Pune |
| 3 | Finance | Mumbai |
| 4 | Sales | Indore |
| 5 | Admin | Delhi |
| 6 | Research | Bangalore |

---

### Table 2: `employee`

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `emp_id` | `INT` | Employee ID |
| `emp_name` | `VARCHAR(30)` | Employee Name |
| `salary` | `DECIMAL(10,2)` | Employee Salary |
| `dept_id` | `INT` | Department ID |

#### Data

| emp_id | emp_name | salary | dept_id |
| :--- | :--- | :--- | :--- |
| 101 | Amit | 30000.00 | 1 |
| 102 | Rahul | 50000.00 | 2 |
| 103 | Priya | 40000.00 | 2 |
| 104 | Neha | 60000.00 | 3 |
| 105 | Rohit | 35000.00 | 3 |
| 106 | Sneha | 45000.00 | 4 |
| 107 | Karan | 55000.00 | 4 |
| 108 | Pooja | 28000.00 | 1 |
| 109 | Vijay | 70000.00 | 2 |
| 110 | Ankit | 32000.00 | 5 |
| 111 | Meena | 65000.00 | 3 |
| 112 | Arjun | 25000.00 | 5 |

> **Note:** Department `6` (Research) currently has no assigned employees.

---

## Assignment Questions

### Part 1: Basic Subqueries & Filtering (Q1 – Q25)

1. **Q1.** Display all employees whose salary is greater than the average salary of all employees.
2. **Q2.** Display the employee or employees who receive the highest salary in the company.
3. **Q3.** Display the employee or employees who receive the lowest salary in the company.
4. **Q4.** Display all employees whose salary is greater than the salary of Amit.
5. **Q5.** Display all employees whose salary is less than the salary of Rahul.
6. **Q6.** Display employees who work in departments located in Indore.
   - *Expected columns:* `emp_id`, `emp_name`, `salary`, `dept_id`
7. **Q7.** Display employees who work in the IT or Finance departments. Obtain the department IDs using a subquery (do not hardcode values such as `2, 3`).
8. **Q8.** Display employees who do not work in departments located in Indore.
9. **Q9.** Display departments that currently have no employees.
10. **Q10.** Display employees whose salary is greater than the average salary of the IT department.
11. **Q11.** Display employees whose salary is greater than the average salary of the Finance department.
12. **Q12.** Display employees whose salary is equal to the highest salary in the IT department.
13. **Q13.** Display employees whose salary is less than the lowest salary in the Sales department.
14. **Q14.** Display employees whose salary is greater than at least one employee working in the HR department.
15. **Q15.** Display employees whose salary is greater than every employee working in the HR department.
16. **Q16.** Display employees whose salary is less than at least one employee working in the IT department.
17. **Q17.** Display employees whose salary is greater than every employee working in the Finance department.
18. **Q18.** Display employees whose salary is below the salary of every employee working in the IT department.
19. **Q19.** Display employees whose salary is greater than their own department's average salary.
20. **Q20.** Display employees whose salary is less than their own department's average salary.
21. **Q21.** Display employees whose salary is exactly equal to their own department's average salary.
22. **Q22.** Display the employee or employees who receive the highest salary in each department.
    - *Expected columns:* `emp_id`, `emp_name`, `salary`, `dept_id`
23. **Q23.** Display the employee or employees who receive the lowest salary in each department.
24. **Q24.** Display employees who are not the highest-paid employees of their respective departments.
25. **Q25.** Display employees who are not the lowest-paid employees of their respective departments.

---

### Part 2: Rankings, Existence, & Correlated Subqueries (Q26 – Q50)

26. **Q26.** Display the second-highest salary in the company without using `LIMIT`.
27. **Q27.** Display the employee or employees having the second-highest salary without using `LIMIT`.
28. **Q28.** Display the third-highest salary in the company without using `LIMIT`.
29. **Q29.** Display the employee or employees having the third-highest salary.
30. **Q30.** Display all departments for which at least one employee exists.
31. **Q31.** Display all departments for which no employee exists.
32. **Q32.** Display departments where at least one employee earns more than 60,000.
33. **Q33.** Display departments where no employee earns more than 60,000.
34. **Q34.** Display departments where at least one employee earns less than 30,000.
35. **Q35.** Display departments where no employee earns less than 30,000.
36. **Q36.** Display employees who belong to a department that exists in the `department` table.
37. **Q37.** Display employees whose salary is greater than their own department's average salary using a correlated subquery.
38. **Q38.** Display employees whose salary is the maximum salary of their department using a correlated subquery.
39. **Q39.** Display employees whose salary is the minimum salary of their department using a correlated subquery.
40. **Q40.** Display each employee along with the average salary of their department.
    - *Expected columns:* `emp_id`, `emp_name`, `salary`, `dept_id`, `department_average_salary`
41. **Q41.** Display each employee along with the highest salary in their department.
    - *Expected columns:* `emp_id`, `emp_name`, `salary`, `dept_id`, `department_highest_salary`
42. **Q42.** Display each employee along with the lowest salary in their department.
    - *Expected columns:* `emp_id`, `emp_name`, `salary`, `dept_id`, `department_lowest_salary`
43. **Q43.** Display each employee along with the company's overall average salary.
    - *Expected columns:* `emp_id`, `emp_name`, `salary`, `company_average_salary`
44. **Q44.** Display each employee along with the difference between their salary and the company's average salary.
    - *Expected columns:* `emp_id`, `emp_name`, `salary`, `salary_difference`
45. **Q45.** Display each employee along with the name of their department, obtaining the department name via a subquery.
    - *Expected columns:* `emp_id`, `emp_name`, `salary`, `dept_name`
46. **Q46.** Display departments whose average salary is greater than the average salary of the entire company.
47. **Q47.** Display departments whose average salary is less than the average salary of the entire company.
48. **Q48.** Display the department having the highest average salary.
49. **Q49.** Display the department having the lowest average salary.
50. **Q50.** Display employees who work in the department having the highest average salary.

---

### Part 3: Advanced Departmental & Salary Aggregations (Q51 – Q80)

51. **Q51.** Display employees who work in the department having the lowest average salary.
52. **Q52.** Display departments having more employees than the average number of employees per department.
53. **Q53.** Display departments where every employee earns more than 30,000.
54. **Q54.** Display departments where at least one employee earns more than 50,000 and at least one employee earns less than 35,000.
55. **Q55.** Display departments where every employee earns less than 70,000.
56. **Q56.** Display employees whose salary is greater than the average of all department average salaries.
57. **Q57.** Display the department whose maximum employee salary is the highest among all departments.
58. **Q58.** Display the department whose minimum employee salary is the lowest among all departments.
59. **Q59.** Display employees whose salary is greater than the maximum salary of the HR department.
60. **Q60.** Display employees whose salary is less than the minimum salary of the Finance department.
61. **Q61.** Display employees whose salary is greater than every employee in HR but less than the salary of at least one employee in IT.
62. **Q62.** Display employees whose salary is greater than at least one employee in Finance but less than every employee in IT.
63. **Q63.** Display employees who work in departments where the department's average salary is greater than 40,000.
64. **Q64.** Display departments where the average salary is greater than 40,000 and at least one employee earns more than 60,000.
65. **Q65.** Display employees whose salary is greater than their department's average salary but less than the company's overall average salary.
66. **Q66.** Display employees whose salary is less than their department's average salary but greater than the company's overall average salary.
67. **Q67.** Display the highest-paid employee from each department without using `GROUP BY` to directly select the employee.
68. **Q68.** Display the second-highest salary employee from each department.
69. **Q69.** Display departments that have at least two employees.
70. **Q70.** Display employees working in departments that have more employees than the HR department.
71. **Q71.** Display employees working in departments that have fewer employees than the IT department.
72. **Q72.** Display the department(s) having the same average salary as the Finance department.
73. **Q73.** Display employees whose salary is equal to the highest salary of any department other than their own department.
74. **Q74.** Display employees whose salary is greater than the average salary of every department.
75. **Q75.** Display employees whose salary is greater than the average salary of at least one department.
76. **Q76.** Display the employee whose salary is closest to the company's average salary.
77. **Q77.** Display the department whose average salary is closest to the company's overall average salary.
78. **Q78.** Display employees who are earning more than the average salary of all employees but are not the highest-paid employee.
79. **Q79.** Display employees who earn more than the average salary of their department and whose department has at least two employees.
80. **Q80.** Find employees who satisfy **all** of the following conditions:
    1. Salary is greater than the company average salary.
    2. Salary is greater than their department average salary.
    3. Their department has at least two employees.
    4. They are not the highest-paid employee in the company.

---

### Part 4: Challenge Questions (Q81 – Q90)

81. **Q81.** Find the department having the second-highest average salary.
82. **Q82.** Find the employee working in the department having the second-highest average salary.
83. **Q83.** Find the second-highest salary employee from every department.
84. **Q84.** Find the department having the second-highest maximum salary.
85. **Q85.** Find employees whose salary is greater than the average salary of the department having the second-highest average salary.
86. **Q86.** Find the employee(s) whose salary is closest to the highest salary in the company without being the highest-paid employee.
87. **Q87.** Find departments where the difference between the highest and lowest salary is greater than 30,000.
88. **Q88.** Find employees whose salary is above their department average and whose salary difference from the department average is greater than 10,000.
89. **Q89.** Find the department(s) where the highest-paid employee earns more than the highest-paid employee of the HR department.
90. **Q90.** Find employees who earn more than every employee in HR, Finance, and Sales.

---

### Part 5: Final Interview Challenge (Q91 – Q100)

91. **Q91.** Find the employee having the third-highest distinct salary without using `JOIN`, `LIMIT`, or `WINDOW FUNCTIONS`.
92. **Q92.** Find the employee having the second-highest salary in each department without using `LIMIT` or `WINDOW FUNCTIONS`.
93. **Q93.** Find the department(s) in which every employee earns more than the company's average salary.
94. **Q94.** Find the department(s) in which at least one employee earns more than the company's average salary and at least one employee earns less than the company's average salary.
95. **Q95.** Find employees whose salary satisfies **all** of the following conditions:
    1. Greater than their department average.
    2. Greater than the company average.
    3. Less than the highest salary in the company.
96. **Q96.** Find the department having the highest average salary, and display all employees belonging to that department along with their salary.
97. **Q97.** Find the department having the lowest average salary, and display all employees belonging to that department.
98. **Q98.** Find the department with the highest number of employees, and display all employees belonging to that department.
99. **Q99.** Find the department with the lowest number of employees (excluding departments having zero employees), and display its employees.
100. **Q100.** Find employees who satisfy **all** of the following conditions:
     1. Salary is above their department average.
     2. Salary is above the company average.
     3. Employee is not the highest-paid employee of their department.
     4. Employee works in a department having at least 2 employees.  
     - *Expected columns:* `emp_id`, `emp_name`, `salary`, `dept_id`