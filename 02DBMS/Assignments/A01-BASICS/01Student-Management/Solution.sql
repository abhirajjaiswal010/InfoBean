

-- ASSIGNMENT 1: STUDENT MANAGEMENT SYSTEM


-- Q1. Create and use database

CREATE DATABASE if NOT exists school_db;

USE school_db;


-- Q2. Create student table

CREATE TABLE if NOT exists student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    city VARCHAR(50),
    marks INT
);


-- Q3. Insert 10 student records

INSERT ignore INTO student (student_name, age, course, city, marks)
VALUES
    ('Rahul Sharma', 21, 'Python', 'Indore', 85),
    ('Priya Verma', 22, 'Java', 'Bhopal', 78),
    ('Amit Singh', 20, 'Python', 'Indore', 92),
    ('Neha Patel', 23, 'Java', 'Pune', 81),
    ('Rohit Mehta', 21, 'Python', 'Mumbai', 88),
    ('Sneha Jain', 22, 'Java', 'Indore', 76),
    ('Karan Gupta', 20, 'Python', 'Delhi', 95),
    ('Pooja Mishra', 23, 'Java', 'Bhopal', 84),
    ('Ankit Tiwari', 21, 'Python', 'Pune', 79),
    ('Riya Kapoor', 22, 'Java', 'Mumbai', 91);


-- Q4. Display student table structure

DESC student;


-- Q5. Display all student records

SELECT * FROM student;


DROP DATABASE school_db;
SELECT "DB is deleted" AS message;
