CREATE DATABASE if NOT EXISTS a011;
use a011;

CREATE TABLE if NOT EXISTS customer
(
    cust_id INT ,
    cust_name varchar(50)
);

CREATE TABLE if NOT EXISTS orders
(
    order_id INT ,
    cust_id INT,
    order_date date,
    total_amount decimal(10,2)
);

INSERT ignore INTO customer (cust_id, cust_name)
VALUES
(101, 'Abhiraj'),
(102, 'Rahul'),
(103, 'Priya'),
(104, 'Aman'),
(105, 'Sneha'),
(106, 'Vikas'),
(107, 'Neha'),
(108, 'Rohit'),
(109, 'Anjali'),
(110, 'Karan');

INSERT INTO orders (order_id, cust_id, order_date, total_amount)
VALUES
(201, 101, '2026-01-10', 2500.00),
(202, 102, '2026-01-12', 1500.50),
(203, 101, '2026-01-15', 3200.00),
(204, 103, '2026-01-18', 4500.00),
(205, 104, '2026-01-20', 1200.00),
(206, 105, '2026-01-22', 5600.75),
(207, 102, '2026-01-25', 2100.00),
(208, 106, '2026-02-01', 3500.00),
(209, 107, '2026-02-05', 1800.00),
(210, 103, '2026-02-08', 2750.00),
(211, 108, '2026-02-10', 6200.00),
(212, 101, '2026-02-12', 900.00),
(213, 109, '2026-02-15', 4100.00),
(214, 105, '2026-02-18', 3300.00),
(215, 108, '2026-02-20', 1500.00);

SELECT * FROM orders;
SELECT * FROM customer;

