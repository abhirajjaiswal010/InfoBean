CREATE DATABASE if NOT EXISTS A06;
use a06;
DROP TABLE IF EXISTS student;
CREATE TABLE if NOT EXISTS student(
    student_id INT primary key,
    name varchar(50) NOT null,
    age INT check (
        age BETWEEN 18 AND 25
    ),
    marks decimal(5, 2) check (
        marks BETWEEN 0 AND 100
    )
);
INSERT into student (student_id, name, age, marks)
values (101, 'alice', 20, 85.5),
    (102, 'bob', 17, 90.0),
    (103, 'charlie', 22, 105.0),
    (104, 'david', 24, 75.0);
SELECT *
FROM student;


DROP TABLE if exists patient;
CREATE TABLE if NOT exists patient(
    patient_id INT primary key,
    patient_name varchar(50) NOT null,
    age INT check(
        age BETWEEN 1 AND 100
    ),
    AdmissionStatus ENUM('Admitted', 'Discharged') DEFAULT 'Admitted',
    treatmentCost decimal(10, 2) check (treatmentCost >= 1000)
);
INSERT into patient(
        patient_id,
        patient_name,
        age,
        AdmissionStatus,
        treatmentCost
    )
values(201, "michael", 25, "admitted", 5000),
    (202, "linda", 105, "admitted", 8000),
    (203, "david", 40, default, 1200),
    (204, "sarah", 30, "discharged", 700);
SELECT *
FROM patient;


DROP TABLE IF EXISTS gymMembers;
CREATE TABLE gymMembers (
    memberId INT PRIMARY KEY,
    memberName VARCHAR(50) NOT NULL,
    membershipType ENUM('Basic', 'Premium', 'VIP') DEFAULT 'Basic',
    monthlyFee DECIMAL(10, 2) CHECK (monthlyFee >= 500)
);
INSERT INTO gymMembers (memberId, memberName, membershipType, monthlyFee)
VALUES (501, 'John', 'Premium', 1200),
    (502, 'Emma', 'VIP', 800),
    (503, 'Daniel', DEFAULT, 700),
    (504, 'Sophia', 'VIP', 300);
SELECT *
FROM gymMembers;