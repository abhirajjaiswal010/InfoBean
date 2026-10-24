# EMPLOYEE PAYROLL AND JOB MANAGEMENT SYSTEM

A company wants to maintain employee information in MySQL. You have been asked to design an `employee` table that strictly enforces the company's data rules using `NOT NULL`, `UNIQUE`, and `CHECK` constraints.

## 1. CREATE THE EMPLOYEE TABLE

Create a table named `employee` with the following columns.

| Column Name | Data Type | Requirements |
|---|---|---|
| `emp_id` | INT | Primary Key, Auto Increment |
| `emp_name` | VARCHAR(50) | Mandatory |
| `email` | VARCHAR(100) | Mandatory and must be unique |
| `phone` | VARCHAR(15) | Mandatory and must be unique |
| `department` | VARCHAR(30) | Mandatory |
| `designation` | VARCHAR(30) | Mandatory |
| `age` | INT | Mandatory, employee must be between 21 and 60 |
| `salary` | DECIMAL(10,2) | Mandatory, salary must be greater than 15000 |
| `experience` | INT | Mandatory, experience must be between 0 and 35 years |
| `joining_year` | INT | Mandatory |
| `status` | VARCHAR(20) | Mandatory, only `Active`, `Inactive`, or `On Leave` |
| `bonus` | DECIMAL(10,2) | Mandatory, cannot be negative |

## 2. APPLY THE CONSTRAINTS

### 2.1 NOT NULL Constraints

The following columns cannot contain `NULL` values:

- `emp_name`
- `email`
- `phone`
- `department`
- `designation`
- `age`
- `salary`
- `experience`
- `joining_year`
- `status`
- `bonus`

### 2.2 UNIQUE Constraints

The following values must be unique across all employees:

- `email`
- `phone`

**Rule:** Two employees cannot have the same email address or phone number.

### 2.3 CHECK Constraints on Individual Columns

Implement the following rules using `CHECK` constraints:

1. **Age:** Must be between 21 and 60, inclusive.
2. **Salary:** Must be greater than 15000.
3. **Experience:** Must be between 0 and 35 years, inclusive.
4. **Bonus:** Must be greater than or equal to 0.
5. **Status:** Can only be `Active`, `Inactive`, or `On Leave`.

## 3. COMBINATION CHECK CONSTRAINTS

Implement the following business rules using `CHECK` constraints involving multiple columns where required.

### Rule 1: Experience and Age

An employee cannot have more experience than is realistically possible based on their age.

**Condition:** `experience` must be less than or equal to `age - 21`.

Examples:

- Age 25 and Experience 4 → Valid
- Age 25 and Experience 10 → Invalid

### Rule 2: Salary and Experience

Employees with more experience must receive an appropriate minimum salary.

**Condition:** If `experience` is greater than or equal to 10, `salary` must be greater than or equal to 50000.

Examples:

- Experience 12 and Salary 60000 → Valid
- Experience 12 and Salary 35000 → Invalid

### Rule 3: Department and Designation

The company allows only the following department-designation combinations.

| Department | Allowed Designations |
|---|---|
| IT | Developer, Tester, Team Lead |
| HR | HR Executive, HR Manager |
| Finance | Accountant, Finance Manager |
| Sales | Sales Executive, Sales Manager |

Implement this rule using a `CHECK` constraint involving both `department` and `designation`.

Examples:

- IT and Developer → Valid
- IT and HR Manager → Invalid
- HR and Developer → Invalid
- Finance and Accountant → Valid

### Rule 4: Status and Bonus

Apply the following business rules:

1. **Active:** Employees can receive a bonus, subject to the general bonus constraints.
2. **Inactive:** Bonus must be equal to 0.
3. **On Leave:** Bonus cannot exceed 20% of the employee's salary.

Examples:

- Active, Salary 50000, Bonus 10000 → Valid
- Inactive, Salary 50000, Bonus 5000 → Invalid
- Inactive, Salary 50000, Bonus 0 → Valid
- On Leave, Salary 50000, Bonus 10000 → Valid
- On Leave, Salary 50000, Bonus 15000 → Invalid

### Rule 5: Joining Year and Experience

Assume the current year is **2026**.

Apply the following rules:

1. The employee's experience cannot exceed the number of years since joining.
2. `joining_year` cannot be greater than 2026.

Examples:

- Joining Year 2020 and Experience 6 → Valid
- Joining Year 2020 and Experience 10 → Invalid
- Joining Year 2027 → Invalid

## 4. INSERT VALID RECORDS

Insert at least **10 valid employee records** into the `employee` table.

Ensure that all records satisfy every individual and combination constraint simultaneously.

Your records must cover:

- Multiple departments
- Multiple designations
- Different experience levels
- Different salary ranges
- All three statuses: `Active`, `Inactive`, and `On Leave`
- Different bonus values

Ensure that every employee has a unique email address and phone number.

## 5. CONSTRAINT TESTING

After inserting the valid records, deliberately execute at least **12 invalid `INSERT` statements** to verify that the constraints work correctly.

Each invalid insertion should violate the intended constraint while keeping other values valid wherever possible.

### 5.1 NOT NULL Testing

Test the following cases:

1. Try inserting `NULL` into `emp_name`.
2. Try inserting `NULL` into `email`.
3. Try inserting `NULL` into `salary`.

### 5.2 UNIQUE Testing

Test the following cases:

4. Try inserting a duplicate email address.
5. Try inserting a duplicate phone number.

### 5.3 Individual CHECK Testing

Test the following cases:

6. Try inserting an employee with age equal to 18.
7. Try inserting an employee with salary equal to 10000.
8. Try inserting an employee with experience equal to -2.
9. Try inserting an employee with bonus equal to -500.
10. Try inserting an employee with status equal to `Retired`.

### 5.4 Combination CHECK Testing

Test the following cases:

11. Try inserting an employee with age 25 and experience 10.
12. Try inserting an employee with experience 12 and salary 35000.
13. Try inserting an employee with department `IT` and designation `HR Manager`.
14. Try inserting an employee with status `Inactive` and bonus 5000.
15. Try inserting an employee with status `On Leave`, salary 50000, and bonus 15000.
16. Try inserting an employee with joining year 2020 and experience 10.
17. Try inserting an employee with joining year 2027.

### Expected Outcome

- All valid employee records should be inserted successfully.
- Every invalid insertion should be rejected by the appropriate constraint.
- Identify the constraint responsible for rejecting each invalid insertion.
- Verify that the table contains only valid employee records after testing.
