-- QNO 3: Alter Students Table
-- Tasks:
-- 1. Add a column dob DATE.
-- 2. Rename column phone to mobile_number.
-- 3. Modify column age to SMALLINT.
-- 4. Drop column email.

desc student ;

ALTER TABLE student 
add column dob DATE;

ALTER TABLE student
rename column phone to mobile_number;

ALTER TABLE student
modify column age SMALLINT;

ALTER TABLE student
DROP column email;

desc student;

