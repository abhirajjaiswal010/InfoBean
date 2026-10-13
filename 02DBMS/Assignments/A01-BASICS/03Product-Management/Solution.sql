-- Assignment 03: Product Management System

-- Question 01: Create and use database
CREATE DATABASE shop_db;

USE shop_db;


-- Question 02: Create product table
CREATE TABLE product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(50),
    category VARCHAR(50),
    brand VARCHAR(50),
    price INT,
    quantity INT
);

-- Question 03: Insert 10 product records
INSERT INTO product
    (product_name, category, brand, price, quantity)
VALUES
    ('Laptop', 'Electronics', 'Dell', 55000, 10),
    ('Smartphone', 'Electronics', 'Samsung', 25000, 15),
    ('Keyboard', 'Accessories', 'Logitech', 1500, 25),
    ('Mouse', 'Accessories', 'HP', 800, 30),
    ('Monitor', 'Electronics', 'LG', 18000, 12),
    ('Headphones', 'Accessories', 'Sony', 3000, 20),
    ('Printer', 'Electronics', 'Canon', 12000, 8),
    ('Tablet', 'Electronics', 'Lenovo', 22000, 14),
    ('Webcam', 'Accessories', 'Logitech', 2500, 18),
    ('Speaker', 'Accessories', 'JBL', 4500, 16);


-- Question 04: Display table structure
DESC product;


-- Question 05: Display all product records
SELECT * FROM product;