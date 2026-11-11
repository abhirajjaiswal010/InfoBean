-- Query 1: Left Join with Unmatched Records
-- Problem Statement:

-- A retail store wants to generate a report displaying all customers and their order details. The report must include customers who have not placed any orders.

-- Task:

-- Write an SQL query using a LEFT JOIN to display all customers along with their order details, ensuring that customers with no orders are still included in the result.

SELECT c.cust_id,c.cust_name,
o.order_date,o.total_amount
FROM customer c
LEFT JOIN orders o 
on c.cust_id=o.cust_id;