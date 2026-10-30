# MySQL Assignment: GROUP BY, HAVING, ORDER BY and Aggregate Functions

## Assignment 1: Employee Salary Analysis

**Table Name:** `employees`

**Note:** Use your friends' names in the given table.

| id | name | department | job_role | salary | hire_date |
|---:|---|---|---|---:|---|
| 1 | Alice | HR | Manager | 6000.00 | 2022-01-15 |
| 2 | Bob | HR | Recruiter | 4000.00 | 2023-03-20 |
| 3 | Charlie | IT | Developer | 5000.00 | 2022-07-25 |
| 4 | David | IT | Developer | 5500.00 | 2021-12-05 |
| 5 | Eve | IT | Tester | 4500.00 | 2023-06-10 |
| 6 | Frank | IT | Tester | 4800.00 | 2023-09-12 |
| 7 | Grace | Finance | Analyst | 5200.00 | 2021-11-18 |
| 8 | Hank | Finance | Analyst | 5300.00 | 2022-04-30 |
| 9 | Ivy | Finance | Manager | 7000.00 | 2023-08-14 |
| 10 | Jack | HR | Recruiter | 4200.00 | 2022-10-05 |

### Questions

1. Find the total number of employees in each department.
2. Find the average salary of employees in each job role.
3. Find the highest salary in the IT department.
4. Find the lowest salary among all employees.
5. Count the number of employees who joined after January 1, 2023.
6. Find the total salary paid in each department.
7. Find the job role that has the highest total salary payout.
8. Find the average salary of employees who joined after 2022.
9. Find departments where the total salary exceeds 10,000.
10. Find the department with the highest number of employees.

---

## Assignment 2: Student Performance Analysis

**Table Name:** `students`

**Note:** Use your friends' names in the given table.

| student_id | name | class | subject | marks | exam_date |
|---:|---|---:|---|---:|---|
| 1 | John | 10 | Math | 85 | 2023-02-10 |
| 2 | Alice | 10 | Science | 78 | 2023-03-15 |
| 3 | Bob | 9 | Math | 92 | 2023-04-20 |
| 4 | David | 9 | Science | 80 | 2023-05-25 |
| 5 | Eve | 10 | Math | 88 | 2023-06-30 |
| 6 | Frank | 9 | Science | 75 | 2023-07-10 |
| 7 | Grace | 10 | Math | 90 | 2023-08-20 |
| 8 | Hank | 9 | Math | 85 | 2023-09-15 |
| 9 | Ivy | 10 | Science | 82 | 2023-10-10 |
| 10 | Jack | 9 | Science | 79 | 2023-11-05 |

### Questions

1. Find the total number of students in each class.
2. Find the highest marks scored in Math.
3. Find the average marks in each subject.
4. Find the total number of students who scored above 80.
5. Find the number of students who took the exam in each month.
6. Find the subject where students scored the highest average marks.
7. Find the student who scored the lowest marks in Science.
8. Find the number of students in each class who scored more than 85.
9. Find the average marks for each subject where the average is above 80.
10. Find the student who scored the highest marks overall.

---

## Assignment 3: Employee Analysis Using GROUP BY, HAVING and ORDER BY

**Use the `employees` table from Assignment 1.**

### Questions

1. Find the total number of employees in each department and display only those departments having more than 2 employees. *(GROUP BY + HAVING)*

2. Find the total salary paid in each department and display the results in descending order of total salary. *(GROUP BY + ORDER BY)*

3. Find the job role that has the highest total salary payout, displaying only roles where total salary is above 10,000. *(GROUP BY + HAVING + ORDER BY)*

4. Find the average salary of employees who joined after 2022, displaying only job roles where the average salary is above 4500. *(WHERE + GROUP BY + HAVING)*

5. Find departments where the total salary exceeds 10,000 and order the results in ascending order of department name. *(GROUP BY + HAVING + ORDER BY)*

---

## Assignment 4: Student Analysis Using GROUP BY, HAVING and ORDER BY

**Use the `students` table from Assignment 2.**

### Questions

1. Find the average marks in each subject and display only subjects where the average is above 80. *(GROUP BY + HAVING)*

2. Find the total number of students in each class and order them by class in descending order. *(GROUP BY + ORDER BY)*

3. Find the subject where students scored the highest average marks, displaying only subjects where the average is above 85. *(GROUP BY + HAVING + ORDER BY)*

4. Find the student who scored the highest marks overall. *(ORDER BY + LIMIT 1)*

5. Find the number of students in each class who scored more than 85, displaying only classes with more than 2 such students. *(GROUP BY + HAVING)*
