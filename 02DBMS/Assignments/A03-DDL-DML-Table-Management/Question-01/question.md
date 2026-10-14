# Assignment 1 — Employee Management System

## Objective
Create an Employee Management System database in MySQL to practice data types, constraints, table creation, data insertion, timestamp behavior, and DDL operations.

## Part 1 — Create Database

1. Create a database named `employee_management`.
2. Select the database for subsequent operations.
3. Display the available databases to verify its creation.

## Part 2 — Create the `employees` Table

Create a table named `employees` with the following columns. Choose the most appropriate MySQL data type for each column.

| No. | Column Name | Requirement |
|---:|---|---|
| 1 | `employee_id` | Unique employee ID; PRIMARY KEY and AUTO_INCREMENT |
| 2 | `employee_code` | Fixed-length employee code |
| 3 | `employee_name` | Employee's full name |
| 4 | `age` | Employee age; must not allow negative values |
| 5 | `number_of_children` | Number of children |
| 6 | `experience_months` | Total professional experience in months |
| 7 | `salary` | Annual salary with exact decimal precision |
| 8 | `performance_score` | Performance score using an approximate decimal value |
| 9 | `productivity_score` | Productivity score using a higher-precision approximate decimal value |
| 10 | `department_id` | Department identification number |
| 11 | `employee_status` | Employment status selected from predefined values |
| 12 | `skills` | Multiple skills selected from predefined values |
| 13 | `gender` | Gender selected from predefined values |
| 14 | `date_of_birth` | Employee's date of birth |
| 15 | `joining_date` | Date the employee joined the company |
| 16 | `login_time` | Daily office login time |
| 17 | `interview_datetime` | Date and time of the employee's interview |
| 18 | `birth_year` | Employee's birth year |
| 19 | `is_active` | Whether the employee is currently active |
| 20 | `short_note` | Very small text information |
| 21 | `employee_description` | Employee description |
| 22 | `training_history` | Larger training-related text |
| 23 | `employee_profile` | Very large employee information |
| 24 | `created_at` | Automatically store the record creation date and time |
| 25 | `updated_at` | Automatically update when the record is modified |

### Required MySQL Data Types

Use every data type listed below at least once in the `employees` table.

**Numeric types:** `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `BIGINT`, `DECIMAL`, `FLOAT`, `DOUBLE`

**String types:** `CHAR`, `VARCHAR`, `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, `LONGTEXT`

**Other types:** `ENUM`, `SET`, `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`, `BOOLEAN`

Also use the following features appropriately:

- `PRIMARY KEY`
- `AUTO_INCREMENT`
- `UNSIGNED`
- `DEFAULT CURRENT_TIMESTAMP`
- `ON UPDATE CURRENT_TIMESTAMP`

**Important:** Do not blindly use `VARCHAR` for every column. Choose data types according to the purpose and expected values of each field.

## Part 3 — Insert Employee Data

Insert at least **15 employees** into the `employees` table.

### 3.1 Employee ID

- Do not manually insert values into `employee_id`.
- Allow MySQL to generate employee IDs using `AUTO_INCREMENT`.

### 3.2 Employee Code

Use fixed-length employee codes such as:

- `EMP001`
- `EMP002`
- `EMP003`

### 3.3 Age

- Insert realistic employee ages, approximately between 22 and 55 years.
- Do not insert negative ages.

### 3.4 Numeric Data

Use varied values for:

- Number of children
- Experience in months
- Annual salary
- Performance score
- Productivity score

Include decimal salary values such as:

- `52500.50`
- `78500.75`
- `125000.25`

### 3.5 Employee Status

Define an `ENUM` containing suitable employment statuses, such as:

- `ACTIVE`
- `INACTIVE`
- `ON_LEAVE`
- `RESIGNED`

Use every status defined in your `ENUM` at least once.

### 3.6 Skills

Use a `SET` to represent multiple skills selected from a predefined list.

Examples:

- `JAVA`
- `PYTHON,MYSQL`
- `JAVA,MYSQL`
- `PYTHON,REACT,AWS`
- `JAVA,PYTHON,MYSQL`

Use different skill combinations across the records.

### 3.7 Gender

Define suitable predefined values using `ENUM` and use every value at least once.

### 3.8 Dates and Times

Insert different values for:

- Date of birth
- Joining date
- Daily login time
- Interview date and time
- Birth year

### 3.9 Boolean Values

Insert both `TRUE` and `FALSE` values for `is_active`.

### 3.10 Text Data

Insert meaningful and varied values for:

- `short_note`
- `employee_description`
- `training_history`
- `employee_profile`

## Part 4 — Verify TIMESTAMP Behavior

Verify the automatic behavior of `created_at` and `updated_at`.

1. Insert a new employee without explicitly providing values for `created_at` and `updated_at`.
2. Display the employee's ID, name, creation timestamp, and update timestamp.
3. Update the employee's name.
4. Display the same columns again.
5. Verify that:
   - `created_at` remains unchanged.
   - `updated_at` changes automatically when the update modifies the record.

Use the following attributes appropriately:

- `DEFAULT CURRENT_TIMESTAMP`
- `ON UPDATE CURRENT_TIMESTAMP`

## Part 5 — DDL Operations

Perform the following operations after creating and inserting data into the `employees` table.

### 5.1 ALTER TABLE

1. Add a `phone_number` column.
2. Add an `email` column.
3. Modify the size of `employee_name`.
4. Modify the size of `employee_code`.
5. Rename `short_note` to `employee_note`.
6. Drop the `email` column.
7. Drop the `phone_number` column.

### 5.2 Add AUTO_INCREMENT Using ALTER TABLE

1. Create a table named `employee_documents`.
2. Initially define `document_id` as a normal integer column without `AUTO_INCREMENT`.
3. Use `ALTER TABLE` to modify `document_id` so that it supports `AUTO_INCREMENT`.
4. Ensure that `document_id` satisfies MySQL's requirements for an auto-increment column.

### 5.3 CREATE TABLE AS SELECT

1. Create a table named `employee_backup` using the existing `employees` table.
2. Copy the employee data into `employee_backup`.
3. Verify the copied records.

### 5.4 TRUNCATE

1. Create a table named `employee_test`.
2. Insert some sample records.
3. Display the records.
4. Execute `TRUNCATE TABLE` on `employee_test`.
5. Display the records again.
6. Verify that the table still exists after truncation.

### 5.5 DROP

1. Drop `employee_test`.
2. Drop `employee_documents`.
3. Verify the remaining tables using `SHOW TABLES`.

## Part 6 — Database Verification

Execute the following MySQL commands:

1. `SHOW DATABASES;`
2. `SHOW TABLES;`
3. `DESC employees;`
4. `SHOW CREATE TABLE employees;`

Finally, verify that:

- All 22 required MySQL data types have been used at least once.
- At least 15 employees have been inserted.
- All required statuses and gender values have been used.
- Multiple skill combinations have been inserted.
- Both `TRUE` and `FALSE` values are present.
- The timestamp behavior works correctly.
- All required DDL operations have been performed.

## Submission Requirements

Submit a single SQL file named:

`Employee_Management_System.sql`

The file must contain the complete solution in execution order, including database creation, table creation, data insertion, timestamp verification, DDL operations, and final verification queries.