### 1. Why does the appointment table contain multiple foreign keys?

An appointment functions as an associative/junction entity that connects multiple independent entities involved in a clinical encounter. It typically references:

* `patient_id`: Identifies which patient is being seen.
* `doctor_id`: Identifies which doctor is conducting the consultation.
* Optional references such as `room_id` or `department_id`: Identifies the physical clinic space or specialty department.

Without these foreign keys, relational integrity across the participating entities cannot be enforced.

---

### 2. Which tables are parent tables and which are child tables?

| Table | Role | Reason |
| --- | --- | --- |
| **Department** | Parent | Referenced by `Doctor`. |
| **Patient** | Parent | Referenced by `Appointment` and `Prescription`. |
| **Doctor** | Parent & Child | Child to `Department`; Parent to `Appointment` and `Prescription`. |
| **Medicine** | Parent | Referenced by `Prescription_Medicine`. |
| **Appointment** | Child (can be Parent) | Child to `Patient` and `Doctor`; Parent if referenced by `Prescription`. |
| **Prescription** | Child & Parent | Child to `Patient`/`Doctor`/`Appointment`; Parent to `Prescription_Medicine`. |
| **Prescription_Medicine** | Child | Pure junction table referencing both `Prescription` and `Medicine`. |

---

### 3. What is the relationship between Patient and Appointment?

* **Cardinality:** **One-to-Many ($1:N$)**
* A single patient can schedule multiple appointments over time ($1$ Patient $\rightarrow$ $N$ Appointments).
* Each individual appointment belongs strictly to one specific patient ($1$ Appointment $\rightarrow$ $1$ Patient).

---

### 4. What is the relationship between Doctor and Appointment?

* **Cardinality:** **One-to-Many ($1:N$)**
* A single doctor can handle multiple appointments with different patients over time ($1$ Doctor $\rightarrow$ $N$ Appointments).
* Each appointment record is assigned to one attending doctor ($1$ Appointment $\rightarrow$ $1$ Doctor).

---

### 5. What is the relationship between Prescription and Medicine?

* **Cardinality:** **Many-to-Many ($M:N$)**
* A single prescription can list multiple medications.
* A single medication can appear on many different prescriptions written for different patients over time.

---

### 6. Why is `prescription_medicine` required?

Relational databases cannot directly implement a Many-to-Many ($M:N$) relationship using standard single-column foreign keys without causing data redundancy, null-padding, or violating First Normal Form (1NF).

`prescription_medicine` serves as an **associative/junction table** that decomposes the $M:N$ relationship into two separate One-to-Many ($1:N$) relationships:

1. `Prescription` ($1$) $\rightarrow$ `Prescription_Medicine` ($N$)
2. `Medicine` ($1$) $\rightarrow$ `Prescription_Medicine` ($N$)

It also holds line-item attributes specific to that pair, such as `dosage`, `frequency`, and `duration_days`.

---

### 7. Why is `prescription_medicine` using a composite primary key?

The composite primary key typically consists of `(prescription_id, medicine_id)`:

1. **Uniqueness Enforcement:** It ensures that the same medication cannot be added to the exact same prescription more than once as separate duplicate rows.
2. **Minimal Overhead:** Both columns are already indexed foreign keys; combining them into a composite primary key eliminates the need for an artificial surrogate key (like an auto-incrementing `id`) while ensuring entity integrity.

---

### 8. Why should deleting a doctor NOT delete historical appointments?

* **Legal and Regulatory Compliance:** Healthcare regulations require medical and audit histories to be retained for statutory periods (often 5–10+ years).
* **Billing and Financial Audits:** Historical appointments back clinic revenue, fee reconciliations, and insurance claims.
* **Patient Continuity of Care:** A patient's medical timeline must preserve when visits occurred, even if the attending physician has retired or left the clinic.

---

### 9. Why is `ON DELETE SET NULL` suitable for `Department -> Doctor`?

A doctor's employment or operational record is independent of a department's reorganization. If a department is dissolved, renamed, or merged, the doctors working in it still exist within the organization. Setting `department_id` to `NULL` preserves the doctor's record, login credentials, and past consultations while reflecting that they are temporarily unassigned to a department.

---

### 10. Why is `ON DELETE CASCADE` suitable for `Patient -> Appointment` in the given test-data scenario?

In automated test suites or development seed workflows:

* Test runs must remain **idempotent and isolated**.
* Tearing down mock data requires wiping all artifacts tied to dummy patients without triggering foreign key constraint violations.
* An appointment has no independent business value without the patient it was booked for, making cascading deletion convenient for cleaning up test fixtures.

---

### 11. Why can `ON DELETE CASCADE` be dangerous for `Medicine -> Prescription_Medicine`?

If a medication is deleted from the `Medicine` catalog (e.g., discontinued or entered by mistake), `ON DELETE CASCADE` will silently and permanently wipe all corresponding line items from historical patient prescriptions.

This creates severe medical risks:

* Historical medical charts will become incomplete or misleading, masking what drug was actually administered to a patient.
* Severe malpractice or adverse-reaction investigations will lack the necessary prescription evidence.
* A safer constraint is `ON DELETE RESTRICT` / `ON DELETE NO ACTION` or soft-deleting using an `is_active = FALSE` flag.

---

### 12. What is the difference between `ON DELETE CASCADE` and `ON DELETE SET NULL`?

* **`ON DELETE CASCADE`:** When the referenced row in the parent table is deleted, the database engine **automatically deletes all corresponding child rows**.
* **`ON DELETE SET NULL`:** When the referenced row in the parent table is deleted, the child rows remain intact, but the foreign key column in those child rows is **set to `NULL**` (requires the foreign key column to be nullable).

---

### 13. What is the difference between `ON UPDATE CASCADE` and `ON UPDATE SET NULL`?

* **`ON UPDATE CASCADE`:** When the primary key value of a parent row is modified, the database engine automatically updates all referencing foreign key values in the child table to match the new value.
* **`ON UPDATE SET NULL`:** When the primary key value of a parent row is modified, the database engine leaves the child rows intact but breaks the link by setting their foreign key columns to `NULL`.

---

### 14. What happens if you try to insert a child record with a non-existing parent ID?

The database engine halts the operation and throws a **Foreign Key Constraint Violation Error** (e.g., SQLSTATE `23503` in PostgreSQL or Error `1452` in MySQL). The transaction fails or rolls back because every non-null foreign key value must match an existing primary/unique key value in the referenced parent table.

---

### 15. What happens if you try to delete a parent record when `ON DELETE RESTRICT` is configured?

The database engine prevents the deletion and throws a **Constraint Violation Error** if one or more child records reference that parent. The parent row cannot be removed until all referencing child rows are either deleted or reassigned to a different parent.