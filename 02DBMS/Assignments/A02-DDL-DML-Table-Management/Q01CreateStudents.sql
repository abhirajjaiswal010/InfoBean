-- QNO 1: Create and Populate Students Table
-- Columns:
-- id INT
-- name VARCHAR(100)
-- age INT
-- gender VARCHAR(10)
-- address VARCHAR(150)
-- phone VARCHAR(15)
-- email VARCHAR(100)

CREATE TABLE if NOT exists  student(
    id INT Unique ,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    address VARCHAR(150),
    phone VARCHAR(15),
    email VARCHAR(100)
);
-- Task: Insert 5 different student records with dummy data.

INSERT ignore INTO student
VALUES
(1, 'Aarav Sharma', 20, 'Male', 'Vijay Nagar, Indore', '9876543210', 'aarav@gmail.com'),
(2, 'Priya Verma', 21, 'Female', 'Palasia, Indore', '9876543211', 'priya@gmail.com'),
(3, 'Rahul Patel', 19, 'Male', 'Bhawarkua, Indore', '9876543212', 'rahul@gmail.com'),
(4, 'Sneha Jain', 22, 'Female', 'Rau, Indore', '9876543213', 'sneha@gmail.com'),
(5, 'Arjun Gupta', 20, 'Male', 'Rajendra Nagar, Indore', '9876543214', 'arjun@gmail.com');

SELECT * FROM student;

