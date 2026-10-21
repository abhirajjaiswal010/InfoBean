CREATE DATABASE if NOT EXISTS empStatusDB;
use empStatusDB;

DROP TABLE if EXISTS staff_update;

CREATE TABLE if NOT exists staff_update(
    staff_id	INT PRIMARY KEY AUTO_INCREMENT,
    staff_name	VARCHAR(50),
    department	VARCHAR(30),
    city	    VARCHAR(30),
    salary	    DECIMAL(10,2),
    experience	INT,
    age	        INT,
    joining_date	DATE,
    status	    VARCHAR(20)

);

INSERT ignore into staff_update 
        (staff_name, department, city, salary, experience, age, joining_date, status)
VALUES
    ('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),
    ('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),
    ('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),
    ('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),
    ('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),
    ('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active');



-- -- ? Q1. Aarav's salary needs to be revised to 52,000. Update his salary using his employee ID.
SELECT "Aarav's salary needs to be revised to 52,000. Update his salary using his employee ID." AS Query_1;

UPDATE staff_update
set salary=52000
WHERE staff_id=1;


-- ? Q2. Bhavna has been transferred to the Finance department in Indore. Update both her department and city.
SELECT "Bhavna has been transferred to the Finance department in Indore. Update both her department and city." AS Query_2;

UPDATE staff_update
set department="finance",
city="indore"
WHERE staff_name="bhavna";



-- -- ? Q3. Give a 4,000 increment to employees whose salary is below 60,000, who have at least 3 years of experience, and who do not belong to Sales.

SELECT "Give a 4,000 increment to employees whose salary is below 60,000, who have at least 3 years of experience, and who do not belong to Sales." AS Query_3;

UPDATE staff_update
set salary=salary+4000
where salary<60000 AND experience>=3 AND department <> "sales";


-- -- ? Q4. Give a 3,000 increment to employees who either belong to IT with at least 3 years of experience or belong to HR with at least 5 years of experience.

SELECT "Give a 3,000 increment to employees who either belong to IT with at least 3 years of experience or belong to HR with at least 5 years of experience." AS Query_4;

UPDATE staff_update
 set salary=salary+3000
 WHERE (department="it" AND experience>=3) OR 
( department="hr" AND experience>=5);



-- -- ? Q5. Give a 10% increment to employees from IT or Finance whose current salary is below 70,000.

SELECT "Give a 10% increment to employees from IT or Finance whose current salary is below 70,000." AS Query_5;

UPDATE staff_update
set salary=salary+(0.1*salary)
WHERE department IN ("it","finance") AND salary<70000;

-- -- ? Q6. Give a 2,500 increment to employees who are neither from HR nor Sales and have between 5 and 8 years of experience.

SELECT "Give a 2,500 increment to employees who are neither from HR nor Sales and have between 5 and 8 years of experience." AS Query_6;

UPDATE staff_update
set salary=salary+2500
WHERE department NOT IN ("hr","sales") AND experience BETWEEN 5 AND 8;

-- -- ? Q7. Give a 5,000 increment to employees whose salary is between 50,000 and 70,000, excluding Finance employees.
SELECT "Give a 5,000 increment to employees whose salary is between 50,000 and 70,000, excluding Finance employees." AS Query_7;

UPDATE staff_update
set salary=salary+5000
WHERE salary BETWEEN 50000 AND 70000 
AND department<>"finance";

-- -- ? Q8. Give a 7% increment to employees whose names start with either A or D.
SELECT "Give a 7% increment to employees whose names start with either A or D." AS Query_8;

UPDATE staff_update
set salary=(1.07*salary)
WHERE staff_name LIKE "A%" OR staff_name LIKE "D%";

-- -- ? Q9. Farah's city is missing. Update her city to Mumbai without modifying employees whose city is already available.
SELECT "Farah's city is missing. Update her city to Mumbai without modifying employees whose city is already available." AS Query_9;

UPDATE staff_update
set city="mumbai"
WHERE staff_name="farah" AND city IS null;

-- -- ? Q10. Give a 10% increment to employees who joined before January 1, 2020 and whose salary is below 70,000.
SELECT "Give a 10% increment to employees who joined before January 1, 2020 and whose salary is below 70,000." AS Query_10;

UPDATE staff_update
SET salary=(1.1*salary)
WHERE joining_date <'2020-01-01' AND salary<70000;


-- -- ? Q11. For IT employees having at least 5 years of experience, increase salary by 8%, increase experience by 1 year, and change their status to Promoted.

SELECT "For IT employees having at least 5 years of experience, increase salary by 8%, increase experience by 1 year, and change their status to Promoted." AS Query_11;


UPDATE staff_update
set salary=(1.08*salary),
experience=experience+1,
status="Promoted"
WHERE department="it" AND experience>=5;

-- -- ? Q12. Give a 6,000 increment to employees having at least 5 years of experience, salary below 75,000, and belonging to either HR or Finance.
SELECT "Give a 6,000 increment to employees having at least 5 years of experience, salary below 75,000, and belonging to either HR or Finance." AS Query_12;


UPDATE staff_update
set salary=salary+6000
WHERE experience>=5 AND salary<75000 AND department IN ("hr","finance");

-- -- ? Q13. Apply the following salary revisions in a single statement: IT → 12%, HR → 9%, Finance → 8%, Sales → 5%.
SELECT "Apply the following salary revisions in a single statement: IT → 12%, HR → 9%, Finance → 8%, Sales → 5%." AS Query_13;

UPDATE staff_update
set salary=
case 
when department="it" then (1.12*salary)
when department="hr" then (1.09*salary)
when department="finance" then (1.08*salary)
when department="sales" then (1.05*salary)
else salary
end;



-- -- ? Q14. Apply salary increments according to experience: 8 or more years → 15%, 5–7 years → 10%, 3–4 years → 7%, less than 3 years → 5%.
SELECT "Apply salary increments according to experience: 8 or more years → 15%, 5–7 years → 10%, 3–4 years → 7%, less than 3 years → 5%." AS Query_14;

UPDATE staff_update
set salary=
case 
when experience>=8 then (1.15*salary)
when experience BETWEEN 5 AND 7 then (1.1*salary)
when experience BETWEEN 3 AND 4 then (1.07*salary)
when experience<3 then (1.05*salary)
else salary
end;


-- -- ? Q15. Apply these salary revisions in a single statement: IT employees with at least 8 years → 18%, other IT employees → 10%, HR employees with at least 6 years → 12%, other HR employees → 7%, Finance employees → 8%, Sales employees → 5%.
SELECT "Apply these salary revisions in a single statement: IT employees with at least 8 years → 18%, other IT employees → 10%, HR employees with at least 6 years → 12%, other HR employees → 7%, Finance employees → 8%, Sales employees → 5%." AS Query_15;

UPDATE staff_update
set salary=
case 
when department="it" AND experience>=8 then (1.18*salary)
when department="it" then (1.1*salary)
when department="hr" AND experience>=6 then (1.12*salary)
when department="hr" then (1.07*salary)
when department="finance" then (1.08*salary)
when department="sales" then (1.05*salary)
else salary
end;


-- -- ? Q16. Update the status of every employee according to salary: 75,000 or more → Senior, 60,000–74,999 → Experienced, 50,000–59,999 → Regular, below 50,000 → Junior.
SELECT "Update the status of every employee according to salary: 75,000 or more → Senior, 60,000–74,999 → Experienced, 50,000–59,999 → Regular, below 50,000 → Junior." AS Query_16;

UPDATE staff_update
set status=
case
when salary>=75000 then "Senior"
when salary BETWEEN 60000 AND 74999 then "Experienced"
when salary BETWEEN 50000 AND 59999 then "Regular"
when salary<50000 then "Junior"
end;

-- -- ? Q17. Display all employees with departments arranged in this business priority: Finance → IT → HR → Sales. Do not change the actual department values.
SELECT "Display all employees with departments arranged in this business priority: Finance → IT → HR → Sales. Do not change the actual department values." AS Query_17;

SELECT * FROM staff_update
ORDER BY
case
when department="finance" then 1
when department="it" then 2
when department="hr" then 3
else 4
End;


-- -- ? Q18. Display all employees with departments arranged in this order: IT → HR → Finance → Sales. Within each department, display the employee with the highest salary first.
SELECT "Display all employees with departments arranged in this order: IT → HR → Finance → Sales. Within each department, display the employee with the highest salary first." AS Query_18;

SELECT * FROM staff_update
ORDER BY
CASE
when department="it" then 1
when department="hr" then 2
when department="finance" then 3
when department="sales" then 4
else 5
end,
salary desc;

-- -- ? Q19. Display employees according to experience priority: 8+ years → 5–7 years → 3–4 years → below 3 years.
SELECT "Display employees according to experience priority: 8+ years → 5–7 years → 3–4 years → below 3 years." AS Query_19;

SELECT * FROM staff_update
ORDER BY
case 
when experience>=8 then 1
when experience BETWEEN 5 AND 7  then 2
when experience BETWEEN 3 AND 4  then 3
else 4
end;



-- -- ? Q20. Give a 5,000 increment to only one employee. The employee must belong to IT or HR, have at least 3 years of experience, and earn less than 70,000. If multiple employees qualify, update only the lowest-paid employee.
SELECT "Give a 5,000 increment to only one employee. The employee must belong to IT or HR, have at least 3 years of experience, and earn less than 70,000. If multiple employees qualify, update only the lowest-paid employee." AS Query_20;

UPDATE staff_update
set salary=salary+5000
WHERE department IN ("hr","it")
AND experience>=3
AND salary<70000
ORDER BY salary ASC
limit 1;


-- -- ? Q21. Give a 10% increment to only one employee. The employee must be Active and have at least 5 years of experience. If multiple employees qualify, update only the highest-paid employee.
SELECT "Give a 10% increment to only one employee. The employee must be Active and have at least 5 years of experience. If multiple employees qualify, update only the highest-paid employee." AS Query_21;

UPDATE staff_update
set salary=(1.1*salary)
WHERE status="active" AND experience>=5
ORDER BY salary desc
limit 1;


-- -- ? Q22. Give a 3,000 increment to only one employee who is neither from HR nor Sales and has at least 3 years of experience. If multiple employees qualify, update the lowest-paid employee.
SELECT "Give a 3,000 increment to only one employee who is neither from HR nor Sales and has at least 3 years of experience. If multiple employees qualify, update the lowest-paid employee." AS Query_22;

UPDATE staff_update
set salary=salary+3000
WHERE department NOT IN ("hr","sales")
AND experience>=3
ORDER BY salary LIMIT 1;



-- -- ? Q23. Change the status to Promoted for only the highest-paid IT employee.
SELECT "Change the status to Promoted for only the highest-paid IT employee." AS Query_23;

update staff_update
set status="Promoted"
WHERE department="it"
ORDER BY salary desc limit 1;


-- -- ? Q24. Give a 12% increment to employees who are either IT employees with at least 5 years of experience or Finance employees earning below 65,000. In addition, only Active employees earning below 80,000 should receive the increment.
SELECT "Give a 12% increment to employees who are either IT employees with at least 5 years of experience or Finance employees earning below 65,000. In addition, only Active employees earning below 80,000 should receive the increment." AS Query_24;

UPDATE staff_update
set salary=(1.12*salary)
WHERE ((department="it" AND experience>=5 )
OR (department="finance" AND salary<65000))
AND status="active" AND salary<80000;



-- -- ? Q25. Apply the following salary revision in one statement: IT + 8 or more years → 18%, other IT employees → 10%, HR + at least 6 years → 12%, other HR employees → 7%, Finance + salary below 65,000 → 10%, Finance + salary 65,000 or above → 7%, Sales + at least 4 years → 6%, all remaining employees → 3%.
SELECT "Apply the following salary revision in one statement: IT + 8 or more years → 18%, other IT employees → 10%, HR + at least 6 years → 12%, other HR employees → 7%, Finance + salary below 65,000 → 10%, Finance + salary 65,000 or above → 7%, Sales + at least 4 years → 6%, all remaining employees → 3%." AS Query_25;


UPDATE staff_update
SET salary = salary * (
    CASE
        WHEN department = 'IT' AND experience >= 8 THEN 1.18
        WHEN department = 'IT' THEN 1.10
        WHEN department = 'HR' AND experience >= 6 THEN 1.12
        WHEN department = 'HR' THEN 1.07
        WHEN department = 'Finance' AND salary < 65000 THEN 1.10
        WHEN department = 'Finance' THEN 1.07
        WHEN department = 'Sales' AND experience >= 4 THEN 1.06
        ELSE 1.03
    END
);



-- -- ? Q26. Update both salary and status according to experience: 8+ years → salary +15%, status Promoted; 5–7 years → salary +10%, status Eligible; 3–4 years → salary +7%, status Regular; below 3 years → salary +5%, status Junior.
SELECT "Update both salary and status according to experience: 8+ years → salary +15%, status Promoted; 5–7 years → salary +10%, status Eligible; 3–4 years → salary +7%, status Regular; below 3 years → salary +5%, status Junior." AS Query_26;

UPDATE staff_update
set salary=
        case
        when experience>=8 then 1.15*salary
        when experience BETWEEN 5 AND 7 then 1.1*salary
        when experience BETWEEN 3 AND 4 then 1.07*salary
        when experience<3 then 1.05*salary
        End
,status =
        case 
        when experience>=8 then "promoted"
        when experience>=5 then "eligible"
        when experience>=3 then "regular"
        else "junior"
        end;

-- -- ? Q27. Change the status to Promoted for employees who have at least 6 years of experience, salary of at least 60,000, are Active, and belong to IT, HR, or Finance.
SELECT "Change the status to Promoted for employees who have at least 6 years of experience, salary of at least 60,000, are Active, and belong to IT, HR, or Finance." AS Query_27;

UPDATE staff_update
SET status = 'Promoted'
WHERE experience >= 6
  AND salary >= 60000
  AND status = 'Active'
  AND department IN ('IT', 'HR', 'Finance');

-- -- ? Q28. Employees belonging to IT, having at least 5 years of experience, and currently living in Pune or Delhi should receive a 10% salary increment, have their city changed to Bangalore, and their status changed to Transferred.
SELECT "Employees belonging to IT, having at least 5 years of experience, and currently living in Pune or Delhi should receive a 10% salary increment, have their city changed to Bangalore, and their status changed to Transferred." AS Query_28;


UPDATE staff_update
SET
    salary = salary * 1.10,
    city = 'Bangalore',
    status = 'Transferred'
WHERE department = 'IT'
  AND experience >= 5
  AND city IN ('Pune', 'Delhi');


-- -- ? Q29. Give a 7,000 special increment to only one eligible employee. The employee must belong to IT, HR, or Finance, have at least 4 years of experience, be Active, and earn less than 75,000. If multiple employees qualify, update only the lowest-paid employee.
-- SELECT "Give a 7,000 special increment to only one eligible employee. The employee must belong to IT, HR, or Finance, have at least 4 years of experience, be Active, and earn less than 75,000. If multiple employees qualify, update only the lowest-paid employee." AS Query_29;


UPDATE staff_update
SET salary = salary + 7000
WHERE department IN ('IT', 'HR', 'Finance')
  AND experience >= 4
  AND status = 'Active'
  AND salary < 75000
ORDER BY salary ASC
LIMIT 1;


-- -- ? Q30. The company wants to perform an annual salary revision using one statement: IT + experience >= 8 + salary >= 70,000 → 18%; IT + experience >= 5 → 12%; HR + experience >= 6 → 10%; HR + experience < 6 → 7%; Finance + salary < 65,000 → 10%; Finance + salary >= 65,000 → 7%; Sales + experience >= 4 → 6%; all remaining employees → 3%. Employees whose status is Inactive must not receive any increment. Additionally, update the status based on the applicable increment: 15% or more → Promoted; 10%–14.99% → Eligible; below 10% → Under Review.
-- SELECT "The company wants to perform an annual salary revision using one statement: IT + experience >= 8 + salary >= 70,000 → 18%; IT + experience >= 5 → 12%; HR + experience >= 6 → 10%; HR + experience < 6 → 7%; Finance + salary < 65,000 → 10%; Finance + salary >= 65,000 → 7%; Sales + experience >= 4 → 6%; all remaining employees → 3%. Employees whose status is Inactive must not receive any increment. Additionally, update the status based on the applicable increment: 15% or more → Promoted; 10%–14.99% → Eligible; below 10% → Under Review." AS Query_30;

UPDATE staff_update
SET
    salary = 
        CASE
            WHEN department = 'IT'
                 AND experience >= 8
                 AND salary >= 70000 THEN 1.18*salary
            WHEN department = 'IT'
                 AND experience >= 5 THEN 1.12*salary
            WHEN department = 'HR'
                 AND experience >= 6 THEN 1.10*salary
            WHEN department = 'HR'
                 AND experience < 6 THEN 1.07*salary
            WHEN department = 'Finance'
                 AND salary < 65000 THEN 1.10*salary
            WHEN department = 'Finance'
                 AND salary >= 65000 THEN 1.07*salary
            WHEN department = 'Sales'
                 AND experience >= 4 THEN 1.06*salary
            ELSE 1.03*salary
        END
    ,
    status = 
        CASE
            WHEN department = 'IT'
                 AND experience >= 8
                 AND salary >= 70000 THEN 'Promoted'
            WHEN department = 'IT'
                 AND experience >= 5 THEN 'Eligible'
            WHEN department = 'HR'
                 AND experience >= 6 THEN 'Eligible'
            WHEN department = 'HR'
                 AND experience < 6 THEN 'Under Review'
            WHEN department = 'Finance'
                 AND salary < 65000 THEN 'Eligible'
            WHEN department = 'Finance'
                 AND salary >= 65000 THEN 'Under Review'
            WHEN department = 'Sales'
                 AND experience >= 4 THEN 'Under Review'
            ELSE 'Under Review'
        END
    
WHERE status = 'Active';
