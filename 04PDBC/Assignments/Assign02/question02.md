# ASSIGNMENT 2: EMPLOYEE MANAGEMENT SYSTEM

## Scenario

A company wants to maintain employee details, departments, salaries, and cities using Python PDBC.

## Table Structure

**Table Name:** `employee_pdbc`

| Column | Data Type |
|---|---|
| eid | INT PRIMARY KEY |
| ename | VARCHAR(50) |
| department | VARCHAR(40) |
| salary | DECIMAL(10,2) |
| city | VARCHAR(30) |

## Sample Data

| eid | ename | department | salary | city |
|---:|---|---|---:|---|
| 201 | Amit | IT | 45000.00 | Indore |
| 202 | Priya | HR | 40000.00 | Bhopal |
| 203 | Rahul | IT | 55000.00 | Indore |
| 204 | Neha | Finance | 50000.00 | Ujjain |
| 205 | Karan | IT | 60000.00 | Indore |

## Menu

```text
===== EMPLOYEE MANAGEMENT SYSTEM =====

1. Add Employee
2. Display All Employees
3. Search Employee by Name
4. Update Employee Salary
5. Delete Employee
6. Exit

Enter your choice:
```

## Tasks

### Task 1: Add Employee

**Input:**
```text
Enter your choice: 1
Enter Employee ID: 206
Enter Employee Name: Anjali
Enter Department: HR
Enter Salary: 42000
Enter City: Dewas
```

**Output:**
```text
Employee inserted successfully.
```

### Task 2: Display All Employees

**Input:**
```text
Enter your choice: 2
```

**Output:**
```text
ID    Name      Department    Salary      City
----------------------------------------------------
201   Amit      IT            45000.00    Indore
202   Priya     HR            40000.00    Bhopal
203   Rahul     IT            55000.00    Indore
204   Neha      Finance       50000.00    Ujjain
205   Karan     IT            60000.00    Indore
206   Anjali    HR            42000.00    Dewas
```

### Task 3: Search Employee by Name Using LIKE

**Input:**
```text
Enter your choice: 3
Enter name to search: ra
```

**Output:**
```text
Matching employees:

ID    Name      Department    Salary      City
----------------------------------------------------
203   Rahul     IT            55000.00    Indore
205   Karan     IT            60000.00    Indore
```

**Note:** Use:

```sql
WHERE ename LIKE %s
```

Pass:

```python
'%' + search_name + '%'
```

### Task 4: Update Employee Salary

**Input:**
```text
Enter your choice: 4
Enter Employee ID: 201
Enter New Salary: 48000
```

**Output:**
```text
Employee salary updated successfully.
```

### Task 5: Delete Employee

**Input:**
```text
Enter your choice: 5
Enter Employee ID: 202
```

**Output:**
```text
Employee deleted successfully.
```

### Task 6: Exit

**Input:**
```text
Enter your choice: 6
```

**Output:**
```text
Thank you for using Employee Management System.
```

---