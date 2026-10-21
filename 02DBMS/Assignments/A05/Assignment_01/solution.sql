CREATE DATABASE if NOT EXISTS employeeDB;
USE employeeDB;

DROP TABLE if exists employees;

CREATE TABLE if NOT EXISTS employees(

    emp_id INT auto_increment primary key ,
    emp_name  varchar(20),
    department varchar(10),
    city varchar(20) , 
    salary decimal(10,2),
    joining_date date,
    experience decimal(5,1),
    age tinyint ,
    gender enum("male","female","other"),
    employment_type enum("FULL_TIME", "PART_TIME", "CONTRACT", "INTERN"),
    skills SET('Java', 'Python', 'JavaScript', 'SQL', 'React', 'HTML', 'CSS'),
    email varchar(100) NULL,
    manager_id INT NULL 
    
);



INSERT INTO employees
(emp_name, department, city, salary, joining_date, experience, age, gender, employment_type, skills, email, manager_id)
VALUES
('Aarav','IT','Indore',75000,'2020-05-15',6,28,'male','FULL_TIME','Java,SQL','aarav@example.com',NULL),
('Priya','HR','Mumbai',45000,'2021-08-10',4,26,'female','FULL_TIME','HTML,CSS','priya@example.com',NULL),
('Rahul','IT','Pune',55000,'2022-03-20',3,25,'male','FULL_TIME','Java,Python,SQL','rahul@example.com',1),
('Sneha','Finance','Indore',38000,'2023-01-12',2,24,'female','CONTRACT','Python,SQL',NULL,2),
('Vikram','IT','Delhi',90000,'2019-11-05',8,32,'male','FULL_TIME','Java,Python,React','vikram@example.com',NULL),
('Ananya','Design','Bhopal',30000,'2024-06-18',1,23,'female','PART_TIME','HTML,CSS,JavaScript',NULL,2),
('Karan','IT','Indore',18000,'2025-07-01',0.5,22,'male','INTERN','Java,SQL','karan@example.com',1),
('Meera','Marketing','Mumbai',52000,'2022-09-14',3.5,27,'female','FULL_TIME','JavaScript,HTML,CSS','meera@example.com',2),
('Rohan','IT','Pune',25000,'2026-01-10',0.25,21,'male','INTERN','Python,SQL',NULL,1),
('Kavya','HR','Delhi',60000,'2020-12-22',5,29,'female','FULL_TIME','JavaScript,HTML','kavya@example.com',NULL),
('Arjun','Finance','Bhopal',42000,'2023-11-08',2.5,26,'male','CONTRACT','Python,SQL,Java','arjun@example.com',2),
('Ishita','IT','Indore',35000,'2024-02-15',1.5,23,'female','PART_TIME','React,JavaScript,CSS',NULL,1),
('Dev','Marketing','Pune',28000,'2025-09-05',0.75,22,'male','CONTRACT','HTML,CSS','dev@example.com',2),
('Pooja','IT','Mumbai',82000,'2021-04-17',6.5,30,'female','FULL_TIME','Java,Python,SQL,React','pooja@example.com',NULL),
('Nikhil','Design','Delhi',48000,'2026-03-01',1,24,'male','PART_TIME','HTML,CSS,JavaScript',NULL,2);



-- ? Q1.Find employees from IT, Finance, or HR who joined after '2023-01-01', have salary between 40,000 and 90,000, and have experience greater than 3 years.

SELECT "Find employees from IT, Finance, or HR who joined after '2023-01-01', have salary between 40,000 and 90,000, and have experience greater than 3 years." AS Query_01;

SELECT * FROM employees
WHERE department IN ("it","finance","hr")
AND joining_date>"2023-01-01" 
AND salary BETWEEN 40000 AND 90000
AND experience>3; 


-- ? Q2. Find employees whose email is NULL, salary is greater than 50,000, and joining date is after '2022-01-01'.

SELECT "Find employees whose email is NULL, salary is greater than 50,000, and joining date is after '2022-01-01'." AS Query_02;

SELECT * FROM employees
WHERE email IS NULL AND
salary > 50000 AND joining_date >"2022-01-01";

-- ? Q3. Find employees whose manager_id is NOT NULL, department is not HR, and salary is either below 40,000 or above 80,000.

SELECT "Find employees whose manager_id is NOT NULL, department is not HR, and salary is either below 40,000 or above 80,000." AS Query_03;

SELECT * FROM employees
WHERE manager_id IS NOT NULL 
AND department <>"hr"
AND (salary <40000 OR salary>80000);

-- ? Q4. Find employees from Indore, Pune, or Delhi who joined between '2022-01-01' and '2025-12-31', have salary greater than 45,000, and experience of at least 3 years.

SELECT "Find employees from Indore, Pune, or Delhi who joined between '2022-01-01' and '2025-12-31', have salary greater than 45,000, and experience of at least 3 years." AS Query_04;

SELECT * FROM employees
WHERE city IN ("indore","pune","delhi")
AND joining_date BETWEEN '2022-01-01' AND '2025-12-31'
AND salary>45000
AND experience >=3;

-- ? Q5. Find employees who are FULL_TIME, have JAVA or PYTHON in their skills, salary greater than 50,000, and email is NOT NULL.

SELECT "Find employees who are FULL_TIME, have JAVA or PYTHON in their skills, salary greater than 50,000, and email is NOT NULL." AS Query_05;

SELECT * FROM employees
WHERE employment_type="full_time"
AND skills IN ("java","python")
AND salary >50000 
AND email IS NOT NULL;

-- ? Q6. Find employees whose name starts with A or S, joining date is after '2023-01-01', salary is between 30,000 and 80,000, and age is between 25 and 35.

SELECT "Find employees whose name starts with A or S, joining date is after '2023-01-01', salary is between 30,000 and 80,000, and age is between 25 and 35." AS Query_06;

SELECT * FROM employees
WHERE (emp_name LIKE "a%" OR emp_name LIKE "s%")
AND joining_date>'2023-01-01'
AND salary BETWEEN 30000 AND 80000
AND age BETWEEN 25 AND 35;


-- ? Q7. Find employees who belong to IT or Finance, have JAVA in skills, experience greater than 4 years, and salary is NOT between 50,000 and 80,000.

SELECT "Find employees who belong to IT or Finance, have JAVA in skills, experience greater than 4 years, and salary is NOT between 50,000 and 80,000." AS Query_07;

SELECT * FROM employees
WHERE department IN ("it","finance")
AND skills ="java"
AND experience>4
AND salary NOT BETWEEN 50000 AND 80000;

-- ? Q8. Find employees whose department is IT, HR, or Marketing, city is not Mumbai, salary is greater than 40,000, and either email is NULL or manager_id is NULL.

SELECT "Find employees whose department is IT, HR, or Marketing, city is not Mumbai, salary is greater than 40,000, and either email is NULL or manager_id is NULL." AS Query_08;

SELECT * FROM employees
WHERE department IN ("it","hr","marketing")
AND city <>"mumbai"
AND salary > 40000 
AND (email IS NULL OR manager_id IS NULL);

-- ? Q9. Find employees who joined after '2022-01-01', are not INTERN, have salary greater than 45,000, and have either SQL or PYTHON in their skills.

SELECT "Find employees who joined after '2022-01-01', are not INTERN, have salary greater than 45,000, and have either SQL or PYTHON in their skills." AS Query_09;

SELECT * FROM employees
WHERE  joining_date>'2022-01-01'
AND employment_type<>"intern"
AND salary>45000
AND (skills="sql" OR skills="python");

-- ? Q10. Find employees whose salary is greater than 60,000 OR experience is greater than 7 years, but exclude employees from Mumbai and Bhopal.

SELECT "Find employees whose salary is greater than 60,000 OR experience is greater than 7 years, but exclude employees from Mumbai and Bhopal." AS Query_10;

SELECT * FROM employees
WHERE (salary>60000 OR experience > 7 ) 
AND city not IN ("mumbai","bhopal");

-- ? Q11. Find employees who joined between '2023-01-01' and '2026-12-31', belong to IT or Development, have salary greater than 50,000, and email is NOT NULL.

SELECT "Find employees who joined between '2023-01-01' and '2026-12-31', belong to IT or Development, have salary greater than 50,000, and email is NOT NULL." AS Query_11;

SELECT * FROM employees
WHERE joining_date '2023-01-01' BETWEEN '2026-12-31' AND '2026-12-31'
AND department in("it","development")
AND  salary>50000 AND email IS NOT null


-- ? Q12. Find employees whose name contains the letter a, department is not HR, salary is between 35,000 and 75,000, and joining date is after '2022-06-01'.

SELECT "Find employees whose name contains the letter a, department is not HR, salary is between 35,000 and 75,000, and joining date is after '2022-06-01'." AS Query_12;

SELECT * FROM employees
WHERE emp_name LIKE "%a%"
AND department <> "hr"
AND salary 35000 AND 75000
AND joining_date>'2022-06-01';


-- ? Q13. Find employees who have both JAVA and SQL skills, salary greater than 55,000, experience greater than 3 years, and manager_id is NOT NULL.

SELECT "Find employees who have both JAVA and SQL skills, salary greater than 55,000, experience greater than 3 years, and manager_id is NOT NULL." AS Query_13;

SELECT * FROM employees
WHERE skills="java" AND skills="sql"
AND salary>55000
AND experience>3
AND manager_id IS NOT null;

-- ? Q14. Find employees who have PYTHON or REACT skills, belong to IT or Development, joined after '2023-01-01', and salary is greater than 50,000.

SELECT "Find employees who have PYTHON or REACT skills, belong to IT or Development, joined after '2023-01-01', and salary is greater than 50,000." AS Query_14;

SELECT * FROM employees
WHERE skills IN ("python","react")
AND department IN ("it","department")
AND joining_date >'2023-01-01' 
AND salary>50000;

-- ? Q15. Find employees whose employment type is CONTRACT or PART_TIME, salary is greater than 35,000, joining date is between '2022-01-01' and '2025-12-31', and email is NOT NULL.

SELECT *
FROM employees
WHERE employment_type IN ('CONTRACT', 'PART_TIME')
  AND salary > 35000
  AND joining_date BETWEEN '2022-01-01' AND '2025-12-31'
  AND email IS NOT NULL;


-- ? Q16. Find employees whose gender is FEMALE, department is IT or Finance, salary is greater than 45,000, and experience is greater than 2 years.

SELECT *
FROM employees
WHERE gender = 'female'
  AND department IN ('IT', 'Finance')
  AND salary > 45000
  AND experience > 2;


-- ? Q17. Find employees whose city is Indore, Pune, or Delhi, department is not HR, joining date is after '2023-01-01', salary is between 40,000 and 100,000, and manager_id is NOT NULL.

SELECT *
FROM employees
WHERE city IN ('Indore', 'Pune', 'Delhi')
  AND department <> 'HR'
  AND joining_date > '2023-01-01'
  AND salary BETWEEN 40000 AND 100000
  AND manager_id IS NOT NULL;


-- ? Q18. Find employees whose salary is NOT between 30,000 and 60,000, experience is greater than 5 years, and department is IT or Finance.

SELECT *
FROM employees
WHERE salary NOT BETWEEN 30000 AND 60000
  AND experience > 5
  AND department IN ('IT', 'Finance');


-- ? Q19. Find employees whose email is NULL OR manager_id is NULL, but salary must be greater than 40,000 and joining date must be after '2022-01-01'.

SELECT *
FROM employees
WHERE (email IS NULL OR manager_id IS NULL)
  AND salary > 40000
  AND joining_date > '2022-01-01';


-- ? Q20. Find employees whose name starts with S OR contains a, department is IT or Finance, salary is between 40,000 and 90,000, and experience is at least 3 years.

SELECT *
FROM employees
WHERE (emp_name LIKE 'S%' OR emp_name LIKE '%a%')
  AND department IN ('IT', 'Finance')
  AND salary BETWEEN 40000 AND 90000
  AND experience >= 3;

-- ? Q21. Find employees who joined between '2022-01-01' and '2025-12-31', are not from Mumbai or Bhopal, have salary greater than 50,000, and have JAVA in their skills.

SELECT "Find employees who joined between '2022-01-01' and '2025-12-31', are not from Mumbai or Bhopal, have salary greater than 50,000, and have JAVA in their skills." AS Query_21;

SELECT *
FROM employees
WHERE joining_date BETWEEN '2022-01-01' AND '2025-12-31'
  AND city NOT IN ('Mumbai', 'Bhopal')
  AND salary > 50000
  AND FIND_IN_SET('JAVA', skills) > 0;


-- -- ? Q22. Find employees who are FULL_TIME, joined after '2023-01-01', have salary greater than 60,000, and have either JAVA + SQL or PYTHON + REACT skills.

SELECT "Find employees who are FULL_TIME, joined after '2023-01-01', have salary greater than 60,000, and have either JAVA + SQL or PYTHON + REACT skills." AS Query_22;

SELECT *
FROM employees
WHERE employment_type = 'FULL_TIME'
  AND joining_date > '2023-01-01'
  AND salary > 60000
  AND (
      (FIND_IN_SET('JAVA', skills) > 0
       AND FIND_IN_SET('SQL', skills) > 0)
      OR
      (FIND_IN_SET('PYTHON', skills) > 0
       AND FIND_IN_SET('REACT', skills) > 0)
  );




-- -- ? Q23. Find employees from IT, Finance, or Development whose salary is between 45,000 and 90,000, experience is greater than 3 years, email is NOT NULL, and manager_id is NOT NULL.

SELECT "Find employees from IT, Finance, or Development whose salary is between 45,000 and 90,000, experience is greater than 3 years, email is NOT NULL, and manager_id is NOT NULL." AS Query_23;

SELECT *
FROM employees
WHERE department IN ('IT', 'Finance', 'Development')
  AND salary BETWEEN 45000 AND 90000
  AND experience > 3
  AND email IS NOT NULL
  AND manager_id IS NOT NULL;

-- -- ? Q24. Find employees whose joining date is after '2023-01-01', department is not HR, salary is greater than 50,000 OR experience is greater than 6 years, and city is not Mumbai.

SELECT "Find employees whose joining date is after '2023-01-01', department is not HR, salary is greater than 50,000 OR experience is greater than 6 years, and city is not Mumbai." AS Query_24;

SELECT *
FROM employees
WHERE joining_date > '2023-01-01'
  AND department <> 'HR'
  AND (salary > 50000 OR experience > 6)
  AND city <> 'Mumbai';

-- -- ? Q25. Find employees whose name starts with A or M, gender is FEMALE, employment type is FULL_TIME, salary is greater than 45,000, and email is NOT NULL.

SELECT "Find employees whose name starts with A or M, gender is FEMALE, employment type is FULL_TIME, salary is greater than 45,000, and email is NOT NULL." AS Query_25;

SELECT *
FROM employees
WHERE (name LIKE 'A%' OR name LIKE 'M%')
  AND gender = 'FEMALE'
  AND employment_type = 'FULL_TIME'
  AND salary > 45000
  AND email IS NOT NULL;

-- -- ? Q26. Find employees who have JAVA or SPRING in their skills, joined after '2022-01-01', salary is NOT between 40,000 and 70,000, and manager_id is NOT NULL.

SELECT "Find employees who have JAVA or SPRING in their skills, joined after '2022-01-01', salary is NOT between 40,000 and 70,000, and manager_id is NOT NULL." AS Query_26;

SELECT *
FROM employees
WHERE (
      FIND_IN_SET('JAVA', skills) > 0
      OR FIND_IN_SET('SPRING', skills) > 0
  )
  AND joining_date > '2022-01-01'
  AND salary NOT BETWEEN 40000 AND 70000
  AND manager_id IS NOT NULL;


-- -- ? Q27. Find employees from Indore, Pune, or Delhi whose joining date is between '2023-01-01' and '2026-12-31', salary is between 40,000 and 100,000, experience is greater than 2 years, and either email or manager_id is NULL.

SELECT "Find employees from Indore, Pune, or Delhi whose joining date is between '2023-01-01' and '2026-12-31', salary is between 40,000 and 100,000, experience is greater than 2 years, and either email or manager_id is NULL." AS Query_27;

SELECT *
FROM employees
WHERE city IN ('Indore', 'Pune', 'Delhi')
  AND joining_date BETWEEN '2023-01-01' AND '2026-12-31'
  AND salary BETWEEN 40000 AND 100000
  AND experience > 2
  AND (email IS NULL OR manager_id IS NULL);

-- -- ? Q28. Find employees belonging to IT or Development, whose name contains a, skills contain JAVA or PYTHON, salary is greater than 50,000, joining date is after '2023-01-01', and email is NOT NULL.

SELECT "Find employees belonging to IT or Development, whose name contains a, skills contain JAVA or PYTHON, salary is greater than 50,000, joining date is after '2023-01-01', and email is NOT NULL." AS Query_28;

SELECT *
FROM employees
WHERE department IN ('IT', 'Development')
  AND name LIKE '%a%'
  AND (
      FIND_IN_SET('JAVA', skills) > 0
      OR FIND_IN_SET('PYTHON', skills) > 0
  )
  AND salary > 50000
  AND joining_date > '2023-01-01'
  AND email IS NOT NULL;

-- --? Q29. Find employees whose department is IT, Finance, or Development, city is not Mumbai or Bhopal, salary is between 40,000 and 90,000, experience is greater than 3 years, skills contain SQL, and manager_id is NOT NULL. Display the result ordered by salary in descending order.

SELECT "Find employees whose department is IT, Finance, or Development, city is not Mumbai or Bhopal, salary is between 40,000 and 90,000, experience is greater than 3 years, skills contain SQL, and manager_id is NOT NULL. Display the result ordered by salary in descending order." AS Query_29;

SELECT *
FROM employees
WHERE department IN ('IT', 'Finance', 'Development')
  AND city NOT IN ('Mumbai', 'Bhopal')
  AND salary BETWEEN 40000 AND 90000
  AND experience > 3
  AND FIND_IN_SET('SQL', skills) > 0
  AND manager_id IS NOT NULL
ORDER BY salary DESC;

-- --? Q30. Find employees whose name starts with S OR contains a, department is IT or Finance, joining date is between '2023-01-01' and '2026-12-31', salary is between 40,000 and 100,000, experience is greater than 2 years, email is NOT NULL, manager_id is NOT NULL, skills contain JAVA or PYTHON, and city is Indore, Pune, or Delhi. Display the result first by department ascending and then by salary descending.

SELECT "Find employees whose name starts with S OR contains a, department is IT or Finance, joining date is between '2023-01-01' and '2026-12-31', salary is between 40,000 and 100,000, experience is greater than 2 years, email is NOT NULL, manager_id is NOT NULL, skills contain JAVA or PYTHON, and city is Indore, Pune, or Delhi. Display the result first by department ascending and then by salary descending." AS Query_30;

SELECT *
FROM employees
WHERE (name LIKE 'S%' OR name LIKE '%a%')
  AND department IN ('IT', 'Finance')
  AND joining_date BETWEEN '2023-01-01' AND '2026-12-31'
  AND salary BETWEEN 40000 AND 100000
  AND experience > 2
  AND email IS NOT NULL
  AND manager_id IS NOT NULL
  AND (
      FIND_IN_SET('JAVA', skills) > 0
      OR FIND_IN_SET('PYTHON', skills) > 0
  )
  AND city IN ('Indore', 'Pune', 'Delhi')
ORDER BY department ASC, salary DESC;




DROP DATABASE employeeDB
