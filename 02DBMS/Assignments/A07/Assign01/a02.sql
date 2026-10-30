CREATE DATABASE IF NOT EXISTS StudentDB;
use StudentDB;

DROP TABLE if EXISTS student;
create TABLE if NOT EXISTS student(

    studentId INT auto_increment primary key,
    name varchar(20),
    class int,
    subject varchar(20),
    marks int,
    examDate Date


);

INSERT into student(name,class,subject,marks,examDate)
VALUES
('John', 10, 'Math', 85, '2023-02-10'),
('Alice', 10, 'Science', 78, '2023-03-15'),
('Bob', 9, 'Math', 92, '2023-04-20'),
('David', 9, 'Science', 80, '2023-05-25'),
('Eve', 10, 'Math', 88, '2023-06-30'),
('Frank', 9, 'Science', 75, '2023-07-10'),
('Grace', 10, 'Math', 90, '2023-08-20'),
('Hank', 9, 'Math', 85, '2023-09-15'),
('Ivy', 10, 'Science', 82, '2023-10-10'),
('Jack', 9, 'Science', 79, '2023-11-05');

-- Query 01 - Find the total number of students in each class.
SELECT "Find the total number of students in each class." AS Query01;

SELECT class,count(*) AS total_student
FROM student
GROUP BY class;

-- Query 02 - Find the highest marks scored in Math.
SELECT "Find the highest marks scored in Math." AS Query02;

SELECT subject,max(marks)
from student
GROUP BY subject
HAVING subject="math";

-- Query 03 - Find the average marks in each subject.
SELECT "Find the average marks in each subject." AS Query03;

SELECT subject,avg(marks) AS avg_marks
FROM student
GROUP BY subject;


-- Query 04 - Find the total number of students who scored above 80.
SELECT "Find the total number of students who scored above 80." AS Query04;

SELECT count(*) AS total_number_student
FROM student
WHERE marks>80;

-- Query 05 - Find the number of students who took the exam in each month.
SELECT "Find the number of students who took the exam in each month." AS Query05;

SELECT monthname(examDate) , count(*)
FROM student
GROUP BY monthname(examDate);



-- Query 06 - Find the subject where students scored the highest average marks.
SELECT "Find the subject where students scored the highest average marks." AS Query06;

SELECT subject,avg(marks) AS avg_marks
FROM student
GROUP BY subject
ORDER BY avg_marks DESC
limit 1;

-- Query 07 - Find the student who scored the lowest marks in Science.
SELECT "Find the student who scored the lowest marks in Science." AS Query07;

SELECT *
FROM student
WHERE subject="science"
ORDER BY marks ASC
limit 1;

-- Query 08 - Find the number of students in each class who scored more than 85.
SELECT "Find the number of students in each class who scored more than 85." AS Query08;

SELECT class,count(*)
FROM student
WHERE marks>85
GROUP BY class;


-- Query 09 - Find the average marks for each subject where the average is above 80.
SELECT "Find the average marks for each subject where the average is above 80." AS Query09;

SELECT subject,avg(marks) AS avg_marks
FROM student
GROUP BY subject
HAVING avg_marks>80;


-- Query 10 - Find the student who scored the highest marks overall.
SELECT "Find the student who scored the highest marks overall." AS Query10;

SELECT *
FROM student
ORDER BY marks DESC
limit 1;