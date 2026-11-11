-- Query 4: Cross-Pairing Analysis
-- Problem Statement:

-- The store wants to analyze every possible combination of customer and order to evaluate all potential customer-order pairings, regardless of whether a transaction actually occurred.

-- Task:

-- Write an SQL query to produce a Cartesian product of the Customer and Orders tables, pairing every customer with every order.

SELECT
    c.cust_id,
    c.cust_name,
    o.order_id,
    o.order_date,
    o.total_amount
FROM customer c
CROSS JOIN orders o;