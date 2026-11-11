# SQL Practice Questions: Customer and Orders

### Database Schema

* **Customer** (`cust_id`, `cust_name`)
* **Orders** (`order_id`, `cust_id`, `order_date`, `total_amount`)

---

### Query 1: Left Join with Unmatched Records

**Problem Statement:**

A retail store wants to generate a report displaying all customers and their order details. The report must include customers who have not placed any orders.

**Task:**

Write an SQL query using a `LEFT JOIN` to display all customers along with their order details, ensuring that customers with no orders are still included in the result.

---

### Query 2: Handling Orphan Orders

**Problem Statement:**

The store wants to generate a report containing all orders placed, even if the associated customer record is missing from the database (i.e., orphan orders caused by data inconsistency).

**Task:**

Write an SQL query to retrieve all orders along with their customer details (if available), ensuring no orders are omitted even when customer records do not exist.

---

### Query 3: Comprehensive Customer and Order Report

**Problem Statement:**

The store wants a comprehensive report displaying all customers and all orders. The output must include:

* Customers who have placed no orders.
* Orders that have missing customer records.
* Customers with matching orders.

**Task:**

Write an SQL query to display all customers and all orders, including unmatched records from both tables.

---

### Query 4: Cross-Pairing Analysis

**Problem Statement:**

The store wants to analyze every possible combination of customer and order to evaluate all potential customer-order pairings, regardless of whether a transaction actually occurred.

**Task:**

Write an SQL query to produce a Cartesian product of the `Customer` and `Orders` tables, pairing every customer with every order.