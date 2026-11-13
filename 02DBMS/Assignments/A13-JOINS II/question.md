# MYSQL JOINS – ASSIGNMENT

## CASE STUDY: COMPANY MANAGEMENT SYSTEM

ABC Technologies wants to develop a Company Management System.

The company wants to generate different reports related to employees, departments, projects, and employee project activities using MySQL JOINs.

You are given the following four tables and their data.

---

# TABLE 1: DEPARTMENT

**Table Name:** `department`

### Structure

| Column Name | Data Type | Description |
|---|---|---|
| dept_id | INT | Department ID |
| dept_name | VARCHAR(30) | Department Name |

### Data

| dept_id | dept_name |
|---|---|
| 1 | HR |
| 2 | IT |
| 3 | Finance |
| 4 | Sales |
| 5 | Marketing |
| 6 | Research |
| 7 | Admin |

---

# TABLE 2: EMPLOYEE

**Table Name:** `employee`

### Structure

| Column Name | Data Type | Description |
|---|---|---|
| emp_id | INT | Employee ID |
| emp_name | VARCHAR(30) | Employee Name |
| salary | DECIMAL(10,2) | Employee Salary |
| dept_id | INT | Department ID |
| manager_id | INT | Manager ID |

### Data

| emp_id | emp_name | salary | dept_id | manager_id |
|---|---|---:|---|---|
| 101 | Amit | 60000 | 1 | NULL |
| 102 | Rahul | 50000 | 2 | 101 |
| 103 | Priya | 42000 | 2 | 101 |
| 104 | Neha | 65000 | 3 | 101 |
| 105 | Rohit | 35000 | 3 | 104 |
| 106 | Sneha | 45000 | 4 | 104 |
| 107 | Karan | 55000 | 4 | 104 |
| 108 | Pooja | 30000 | 1 | 101 |
| 109 | Vijay | 75000 | 2 | 102 |
| 110 | Ankit | 32000 | 5 | 102 |
| 111 | Meena | 68000 | 3 | 104 |
| 112 | Arjun | 25000 | 5 | 110 |
| 113 | Tara | 40000 | NULL | 102 |

---

# TABLE 3: PROJECT

**Table Name:** `project`

### Structure

| Column Name | Data Type | Description |
|---|---|---|
| project_id | INT | Project ID |
| project_name | VARCHAR(50) | Project Name |
| dept_id | INT | Department ID |
| budget | INT | Project Budget |

### Data

| project_id | project_name | dept_id | budget |
|---|---|---|---:|
| 201 | Payroll System | 1 | 200000 |
| 202 | Website Development | 2 | 500000 |
| 203 | Banking Application | 3 | 700000 |
| 204 | CRM System | 4 | 300000 |
| 205 | Inventory System | 5 | 150000 |
| 206 | AI Research | 6 | 900000 |
| 207 | Mobile Application | 2 | 250000 |

---

# TABLE 4: EMPLOYEE_PROJECT

**Table Name:** `employee_project`

### Structure

| Column Name | Data Type | Description |
|---|---|---|
| emp_id | INT | Employee ID |
| project_id | INT | Project ID |
| hours_worked | INT | Total Working Hours |

### Data

| emp_id | project_id | hours_worked |
|---|---|---:|
| 101 | 201 | 20 |
| 102 | 202 | 40 |
| 102 | 207 | 15 |
| 103 | 202 | 30 |
| 104 | 203 | 35 |
| 105 | 203 | 20 |
| 106 | 204 | 25 |
| 107 | 204 | 30 |
| 109 | 202 | 45 |
| 110 | 205 | 20 |
| 111 | 203 | 25 |

---

## IMPORTANT NOTES

1. Department 6 has no employees.
2. Department 7 has no employees and no projects.
3. Employee 113 is not assigned to any department.
4. Some employees are not assigned to any project.
5. Project 206 has no employees assigned.
6. Employee 102 is working on two projects.
7. The employee table contains manager IDs that refer to other employees in the same table.

These records are provided to practice different JOIN conditions.

---

# QUESTIONS

## PART A: INNER JOIN

**Q1.** The HR department wants to display all employees with their respective department names.

Write a query using INNER JOIN.

**Q2.** The IT department wants to see its employees.

Display employee ID, employee name, salary, and department name for employees working in IT.

**Q3.** The company wants to find employees earning more than 50000.

Display employee name, salary, and department name.

**Q4.** The management wants to display all projects along with their department names and budgets.

**Q5.** Display employees who work in the Finance or Sales department.

---

## PART B: LEFT JOIN AND RIGHT JOIN

**Q6.** The HR department wants a complete employee list, including employees who are not assigned to any department.

Write a query using LEFT JOIN.

**Q7.** Find employees who do not belong to any department.

**Q8.** The management wants to see all departments with their employees, including departments that have no employees.

**Q9.** Find the departments that currently have no employees.

**Q10.** The company wants to display all departments and their projects, including departments that have no projects.

Use RIGHT JOIN.

---

## PART C: FULL OUTER JOIN

MySQL does not directly support FULL OUTER JOIN.

**Q11.** The management wants a complete report of all employees and departments.

Display all employees and all departments, including unmatched records.

Use LEFT JOIN, RIGHT JOIN, and UNION.

**Q12.** Find employees without departments and departments without employees in a single result.

Use FULL OUTER JOIN simulation.

---

## PART D: SELF JOIN

**Q13.** The company wants to display each employee's name along with their manager's name.

Use SELF JOIN.

**Q14.** Find employees who do not have any manager.

**Q15.** The management wants to find employees whose salary is greater than their manager's salary.

Display employee name, employee salary, manager name, and manager salary.

**Q16.** Find employees who report to the same manager.

Display both employee names and their manager's name.

---

## PART E: MULTIPLE TABLE JOINS

**Q17.** The project manager wants a report containing employee names, project names, and working hours.

Use the employee, employee_project, and project tables.

**Q18.** Display project names along with their department names and budgets.

**Q19.** The company wants a complete employee project report.

Display employee name, department name, project name, and working hours.

**Q20.** Find employees working on projects having a budget greater than 300000.

Display employee name, project name, and project budget.

---

## PART F: JOIN WITH GROUP BY AND HAVING

**Q21.** Find the total number of employees in each department, including departments having zero employees.

**Q22.** Find the average salary of employees in each department.

Display department name and average salary.

**Q23.** Find the total number of employees working on each project, including projects having zero employees.

**Q24.** The management wants to know the total working hours of each project.

Display project name and total working hours.

**Q25.** Find departments having more than two employees.

Display department name and employee count.

---

## PART G: ADVANCED JOIN QUESTIONS

**Q26.** Find employees who are working on more than one project.

Display employee name and total project count.

**Q27.** Find employees who are not assigned to any project but belong to a department.

**Q28. CROSS JOIN**

The company wants to generate all possible employee and project combinations, whether an employee is actually working on that project or not.

Write a query using CROSS JOIN.

**Q29.** Find the highest-paid employee in each department.

Display employee name, department name, and salary.

**Q30.** The management wants to generate a complete department report containing:

1. Department Name
2. Total Employees
3. Total Projects
4. Total Project Budget
5. Total Working Hours

Include all departments, even if they have no employees or projects.

Make sure that duplicate rows created by multiple JOINs do not affect the aggregate results.

---

# END OF ASSIGNMENT