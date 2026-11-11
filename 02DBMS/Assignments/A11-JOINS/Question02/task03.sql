-- Query 3: Comprehensive Customer and Order Report
-- Problem Statement:

-- The store wants a comprehensive report displaying all customers and all orders. The output must include:

-- Customers who have placed no orders.
-- Orders that have missing customer records.
-- Customers with matching orders.
-- Task:

-- Write an SQL query to display all customers and all orders, including unmatched records from both tables.

SELECT
    c.cust_id,
    c.cust_name,
    o.order_id,
    o.order_date,
    o.total_amount
FROM customer c
LEFT JOIN orders o
ON c.cust_id = o.cust_id

UNION

SELECT
    c.cust_id,
    c.cust_name,
    o.order_id,
    o.order_date,
    o.total_amount
FROM customer c
RIGHT JOIN orders o
ON c.cust_id = o.cust_id;

SELECT
    c.cust_id,
    c.cust_name,
    o.order_id,
    o.order_date,
    o.total_amount
FROM customer c
INner JOIN orders o
ON c.cust_id = o.cust_id;