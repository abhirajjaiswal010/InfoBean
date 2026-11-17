# ASSIGNMENT 3: PRODUCT INVENTORY MANAGEMENT SYSTEM

## Scenario

A retail shop wants to manage product details, prices, categories, and available stock using Python PDBC.

## Concepts to Practice

1. INSERT
2. SELECT
3. UPDATE
4. DELETE
5. LIKE Operator
6. Parameterized Queries
7. commit()
8. fetchall()
9. Menu-Driven Programming
10. WHERE Clause
11. Comparison Operators
12. BETWEEN Operator
13. String Pattern Matching

## Table Structure

**Table Name:** `product_pdbc`

| Column | Data Type |
|---|---|
| pid | INT PRIMARY KEY |
| pname | VARCHAR(60) |
| category | VARCHAR(40) |
| price | DECIMAL(10,2) |
| quantity | INT |

## Sample Data

| pid | pname | category | price | quantity |
|---:|---|---|---:|---:|
| 301 | Laptop | Electronics | 55000.00 | 10 |
| 302 | Mouse | Electronics | 800.00 | 50 |
| 303 | Keyboard | Electronics | 1500.00 | 30 |
| 304 | Notebook | Stationery | 100.00 | 100 |
| 305 | Pen | Stationery | 20.00 | 200 |

## Menu

```text
===== PRODUCT INVENTORY SYSTEM =====

1. Add Product
2. Display All Products
3. Search Product by Name
4. Update Product Price
5. Delete Product
6. Exit

Enter your choice:
```

## Basic CRUD Tasks

### Task 1: Add Product

**Input:**
```text
Enter your choice: 1
Enter Product ID: 306
Enter Product Name: Monitor
Enter Category: Electronics
Enter Price: 12000
Enter Quantity: 15
```

**Output:**
```text
Product inserted successfully.
```

### Task 2: Display All Products

**Input:**
```text
Enter your choice: 2
```

**Output:**
```text
ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics    55000.00    10
302   Mouse         Electronics      800.00    50
303   Keyboard      Electronics     1500.00    30
304   Notebook      Stationery       100.00   100
305   Pen           Stationery        20.00   200
306   Monitor       Electronics    12000.00    15
```

### Task 3: Search Product by Name Using LIKE

**Input:**
```text
Enter your choice: 3
Enter product name to search: o
```

**Output:**
```text
Matching products:

ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics    55000.00    10
302   Mouse         Electronics      800.00    50
304   Notebook      Stationery       100.00   100
306   Monitor       Electronics    12000.00    15
```

**Note:** Use:

```sql
WHERE pname LIKE %s
```

Pass:

```python
'%' + search_name + '%'
```

### Task 4: Update Product Price

**Input:**
```text
Enter your choice: 4
Enter Product ID: 302
Enter New Price: 900
```

**Output:**
```text
Product price updated successfully.
```

### Task 5: Delete Product

**Input:**
```text
Enter your choice: 5
Enter Product ID: 305
```

**Output:**
```text
Product deleted successfully.
```

### Task 6: Exit

**Input:**
```text
Enter your choice: 6
```

**Output:**
```text
Thank you for using Product Inventory System.
```

---

## Additional SQL and PDBC Practice Scenarios

Perform the following operations on the `product_pdbc` table.

### A. Category-Based Searching

**Q1.** Display all products from the Electronics category.

**Q2.** Display all products from the Stationery category.

**Q3.** Display products whose category contains the word `tron`.

### B. LIKE Operator Practice

**Q4.** Search products whose names contain `oo`.

**Q5.** Search products whose names start with `M`.

**Q6.** Search products whose names end with `e`.

### C. Conditional Searching

**Q7.** Display products whose price is greater than 1000.

**Q8.** Display products whose quantity is less than 20.

### D. Update Operations

**Q9.** Update the quantity of a product using its Product ID.

**Q10.** Update the category of a product using its Product ID.

### E. Delete Operations

**Q11.** Delete a product using its Product ID.

### F. Range-Based Searching

**Q12.** Search products within a user-provided price range.

**Input Example:**
```text
Enter minimum price: 500
Enter maximum price: 20000
```

**Expected SQL Condition:**
```sql
WHERE price BETWEEN %s AND %s
```

**Note:** Use parameterized queries for all dynamic values.

---

## Suggested Success Messages

| Operation | Message |
|---|---|
| INSERT | Record inserted successfully. |
| SELECT | Records displayed successfully. |
| UPDATE | Record updated successfully. |
| DELETE | Record deleted successfully. |
| NOT FOUND | No record found for the given ID. |
| INVALID CHOICE | Invalid choice. Please try again. |
| EXIT | Thank you for using the system. |

## Important Instructions

1. Create the required database and tables before executing the programs.
2. Use Python Database Connectivity (PDBC) to connect Python with MySQL.
3. Use parameterized queries (`%s`) for dynamic values.
4. Use `execute()` to execute SQL statements.
5. Use `fetchall()` to retrieve multiple records.
6. Use `commit()` after INSERT, UPDATE, and DELETE operations.
7. Use `rowcount` to check whether UPDATE and DELETE operations affected any records.
8. Use proper exception handling with `try-except`.
9. Close the cursor and database connection after program execution.
10. Implement menu-driven programming using loops and conditional statements.