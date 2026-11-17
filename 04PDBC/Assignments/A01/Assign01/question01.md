# ASSIGNMENT 1: STUDENT MANAGEMENT SYSTEM

## Scenario

A coaching institute wants to manage student records using Python Database Connectivity (PDBC).

## Table Structure

**Table Name:** `student_pdbc`

| Column | Data Type |
|---|---|
| sid | INT PRIMARY KEY |
| sname | VARCHAR(50) |
| course | VARCHAR(50) |
| fees | DECIMAL(10,2) |
| city | VARCHAR(30) |

## Sample Data

| sid | sname | course | fees | city |
|---:|---|---|---:|---|
| 101 | Amit | Python | 15000.00 | Indore |
| 102 | Priya | Java | 18000.00 | Bhopal |
| 103 | Rahul | Python | 15000.00 | Indore |
| 104 | Neha | Java | 18000.00 | Ujjain |
| 105 | Karan | MERN | 20000.00 | Indore |

## Menu

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. Display All Students
3. Search Student by Name
4. Update Student Fees
5. Delete Student
6. Exit

Enter your choice:
```

## Tasks

### Task 1: Add Student

**Input:**
```text
Enter your choice: 1
Enter Student ID: 106
Enter Student Name: Anjali
Enter Course: Python
Enter Fees: 15000
Enter City: Dewas
```

**Output:**
```text
Student inserted successfully.
```

### Task 2: Display All Students

**Input:**
```text
Enter your choice: 2
```

**Output:**
```text
ID    Name      Course    Fees       City
------------------------------------------------
101   Amit      Python    15000.00   Indore
102   Priya     Java      18000.00   Bhopal
103   Rahul     Python    15000.00   Indore
104   Neha      Java      18000.00   Ujjain
105   Karan     MERN      20000.00   Indore
106   Anjali    Python    15000.00   Dewas
```

### Task 3: Search Student by Name Using LIKE

**Input:**
```text
Enter your choice: 3
Enter name to search: an
```

**Output:**
```text
Matching students:

ID    Name      Course    Fees       City
------------------------------------------------
105   Karan     MERN      20000.00   Indore
106   Anjali    Python    15000.00   Dewas
```

**Note:** Use a parameterized query.

```sql
WHERE sname LIKE %s
```

Pass the search pattern:

```python
'%' + search_name + '%'
```

### Task 4: Update Student Fees

**Input:**
```text
Enter your choice: 4
Enter Student ID: 101
Enter New Fees: 17000
```

**Output:**
```text
Student fees updated successfully.
```

### Task 5: Delete Student

**Input:**
```text
Enter your choice: 5
Enter Student ID: 104
```

**Output:**
```text
Student deleted successfully.
```

### Task 6: Exit

**Input:**
```text
Enter your choice: 6
```

**Output:**
```text
Thank you for using Student Management System.
```

---



