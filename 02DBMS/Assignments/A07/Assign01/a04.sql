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


-- Find the average marks in each subject and display only subjects where the average is above 80. (GROUP BY + HAVING)

SELECT subject,avg(marks) AS avg_mark
FROM student
GROUP BY subject
HAVING avg_mark>80;


-- Find the total number of students in each class and order them by class in descending order. (GROUP BY + ORDER BY)

SELECT class,count(*) AS total_student
FROM student
GROUP BY class
ORDER BY class desc;

-- Find the subject where students scored the highest average marks, displaying only subjects where the average is above 85. (GROUP BY + HAVING + ORDER BY)

SELECT subject,avg(marks) AS avg_mark
FROM student
GROUP BY subject
HAVING avg_mark>85
ORDER BY avg_mark DESC;

-- Find the student who scored the highest marks overall. (ORDER BY + LIMIT 1)

SELECT * FROM student
ORDER BY marks DESC
limit 1;



-- Find the number of students in each class who scored more than 85, displaying only classes with more than 2 such students. (GROUP BY + HAVING)

SELECT class,count(*) AS number_of_student
FROM student
WHERE marks>85
GROUP BY class
HAVING number_of_student>2;
