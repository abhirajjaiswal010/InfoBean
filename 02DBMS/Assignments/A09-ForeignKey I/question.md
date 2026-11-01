# MySQL – Foreign Key & Referential Actions Assignment

**Total Assignments: 4**

---

## QNO 1: Employee and Department Management

A company wants to manage its employees and their respective departments. Each employee must belong to a department. If a department is deleted, all employees in that department should also be removed automatically.

### Tasks

**1. Create the Departments Table**
- `DepartmentID` – Primary Key.
- `DepartmentName` – Must be UNIQUE and NOT NULL.

**2. Create the Employees Table**
- `EmployeeID` – Primary Key.
- `EmployeeName` – NOT NULL.
- `Salary` – NOT NULL.
- `DepartmentID` – Foreign Key referencing `Departments(DepartmentID)`.
- If a department is deleted, all employees belonging to that department should also be deleted automatically.

**3. Insert Sample Data**
- Insert at least 3 departments.
- Insert at least 5 employees.
- Ensure at least 2 employees belong to the same department.

**4. Perform the Following Operations**
- Display all employees along with their department names without using JOIN.
- Update an employee's department.
- Delete a department and observe what happens to its employees.

---

## QNO 2: Hospital – Doctors and Patients Management

A hospital wants to store patient records and their assigned doctors. If a doctor leaves, all related patient records should be deleted automatically.

### Tasks

**1. Create the Doctors Table**
- `DoctorID` – Primary Key, AUTO_INCREMENT.
- `DoctorName` – NOT NULL.
- `Specialization` – NOT NULL and UNIQUE.

**2. Create the Patients Table**
- `PatientID` – Primary Key, AUTO_INCREMENT.
- `PatientName` – NOT NULL.
- `DoctorID` – Foreign Key referencing `Doctors(DoctorID)`.
- If a doctor is deleted, all patients assigned to that doctor should also be deleted automatically.

**3. Insert Sample Data**
- Insert at least 3 doctors.
- Insert at least 5 patients.

**4. Perform the Following Operations**
- Delete a doctor and check whether the related patient records are automatically deleted.
- Update a patient's doctor to a new doctor.

---

## QNO 3: Library – Books and Authors Management

A library maintains records of books and their respective authors. If an author is removed, their books should not be deleted. Instead, the author information in the corresponding book records should be set to NULL.

### Tasks

**1. Create the Authors Table**
- `AuthorID` – Primary Key, AUTO_INCREMENT.
- `AuthorName` – NOT NULL and UNIQUE.

**2. Create the Books Table**
- `BookID` – Primary Key, AUTO_INCREMENT.
- `BookTitle` – NOT NULL and UNIQUE.
- `AuthorID` – Foreign Key referencing `Authors(AuthorID)`.
- If an author is deleted, the corresponding `AuthorID` in the Books table should automatically be set to NULL.

**3. Insert Sample Data**
- Insert at least 3 authors.
- Insert at least 5 books.

**4. Perform the Following Operations**
- Delete an author and verify that their books remain in the Books table with `AuthorID` set to NULL.
- Update the author of a book to a new author.

---

## QNO 4: University – Students, Exams and Results Management

A university wants to maintain students' examination results. If a student is deleted, all their associated examination results should also be deleted automatically.

### Tasks

**1. Create the Students Table**
- `StudentID` – Primary Key, AUTO_INCREMENT.
- `StudentName` – NOT NULL.

**2. Create the Exams Table**
- `ExamID` – Primary Key, AUTO_INCREMENT.
- `SubjectName` – NOT NULL and UNIQUE.

**3. Create the Results Table**
- `ResultID` – Primary Key, AUTO_INCREMENT.
- `StudentID` – Foreign Key referencing `Students(StudentID)`.
- `ExamID` – Foreign Key referencing `Exams(ExamID)`.
- `Score` – NOT NULL and CHECK constraint (Score BETWEEN 0 AND 100).
- If a student is deleted, all their associated results should also be deleted automatically.

**4. Insert Sample Data**
- Insert at least 3 students.
- Insert at least 3 exams.
- Insert at least 5 results.

**5. Perform the Following Operations**
- Delete a student and verify that their associated results are automatically deleted.
- Update an exam's subject name and observe the effect.

---

**End of Assignment**