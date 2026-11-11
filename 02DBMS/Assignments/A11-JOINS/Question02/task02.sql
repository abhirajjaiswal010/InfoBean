-- Query 2: Handling Orphan Orders
-- Problem Statement:

-- The store wants to generate a report containing all orders placed, even if the associated customer record is missing from the database (i.e., orphan orders caused by data inconsistency).

-- Task:

-- Write an SQL query to retrieve all orders along with their customer details (if available), ensuring no orders are omitted even when customer records do not exist.

SELECT
    c.cust_id,
    c.cust_name,
    o.order_id,
    o.order_date,
    o.total_amount
FROM orders o
RIGHT JOIN customer c ON
c.cust_id=o.cust_id;