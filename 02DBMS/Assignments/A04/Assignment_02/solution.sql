CREATE DATABASE if NOT EXISTS productManagementSystem;
use productManagementSystem;


CREATE TABLE IF NOT EXISTS product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
    rating TINYINT CHECK (rating BETWEEN 1 AND 5),
    mfg_date DATE,

    CONSTRAINT uq_product_name_brand UNIQUE (product_name, brand)
);

INSERT ignore INTO product
    (product_name, category, brand, city, price, stock, rating, mfg_date)
VALUES
    ('Wireless Mouse', 'Electronics', 'Logitech', 'Indore', 799.00, 50, 4, '2024-03-15'),
    ('Mechanical Keyboard', 'Electronics', 'Logitech', 'Bhopal', 2499.00, 30, 5, '2023-07-20'),
    ('Office Chair', 'Furniture', 'IKEA', 'Pune', 8500.00, 15, 4, '2022-05-10'),
    ('Study Table', 'Furniture', 'Godrej', 'Mumbai', 8500.00, 0, 5, '2025-01-12'),
    ('Cotton T-Shirt', 'Clothing', 'Puma', 'Delhi', 999.00, 100, 4, '2026-02-18'),
    ('Running Shoes', 'Clothing', 'Puma', 'Indore', 2999.00, 25, 5, '2024-08-05'),
    ('Basmati Rice 5kg', 'Grocery', 'India Gate', 'Bhopal', 650.00, 40, 4, '2025-11-22'),
    ('Cooking Oil 5L', 'Grocery', 'Fortune', 'Pune', 750.00, 0, 3, '2026-01-08'),
    ('Smartphone', 'Electronics', 'Samsung', 'Mumbai', 25000.00, 20, 5, '2025-06-14'),
    ('Refrigerator', 'Electronics', 'LG', 'Delhi', 42000.00, 10, 4, '2021-09-25');

SELECT * FROM product;


-- & Question-01 Products priced above ₹30,000 with rating at least 4, excluding Mumbai.
SELECT "Products priced above ₹30,000 with rating at least 4, excluding Mumbai." AS Query_01;

SELECT * FROM product
WHERE price>30000
AND rating>=4
AND city <> "mumbai";

-- & Question-02 Products with stock below 20 or price above ₹75,000, excluding Grocery.
SELECT "Products with stock below 20 or price above ₹75,000, excluding Grocery." AS Query_02;

SELECT * FROM product
WHERE (stock<20 OR price>75000) AND category!="grocery";

-- & Question-03 Products priced between ₹15,000 and ₹60,000, rated 3 to 5, manufactured after 2022.
SELECT "Products priced between ₹15,000 and ₹60,000, rated 3 to 5, manufactured after 2022." AS Query_03;

SELECT*FROM product
WHERE (price BETWEEN 15000 AND 60000) 
AND (rating BETWEEN 3 AND 5) 
AND year(mfg_date) >2022;

-- & Question-04 Products from Indore, Pune, or Delhi, priced above ₹20,000 and in stock.
SELECT "Products from Indore, Pune, or Delhi, priced above ₹20,000 and in stock." AS Query_04;

SELECT * FROM product
WHERE city IN ("indore","pune","delhi") AND price>20000 AND stock>0;

-- & Question-05 Products belonging to Electronics or Furniture.
SELECT "Products belonging to Electronics or Furniture." AS Query_05;

SELECT* FROM product
WHERE category IN ("Electronics","furniture");

-- & Question-06 Products belonging to Electronics, Clothing, or Grocery.
SELECT "Products belonging to Electronics, Clothing, or Grocery." AS Query_06;

SELECT * FROM product
WHERE category IN ("electronics","clothing","grocery");

-- & Question-07 Products not from Indore or Bhopal.
SELECT "Products not from Indore or Bhopal." AS Query_07;

SELECT * FROM product
WHERE city NOT IN ("indore","bhopal");

-- & Question-08 Products whose brand is not Samsung, LG, or Sony.
SELECT "Products whose brand is not Samsung, LG, or Sony." AS Query_08;

SELECT * FROM product
WHERE brand NOT IN ("samsung","lg","sony");

-- & Question-09 Products priced between ₹10,000 and ₹50,000.
SELECT "Products priced between ₹10,000 and ₹50,000." AS Query_09;

SELECT * FROM product
WHERE price BETWEEN 10000 AND 50000;


-- & Question-10 Products with stock between 20 and 60.
SELECT "Products with stock between 20 and 60." AS Query_10;

SELECT * FROM product
WHERE stock BETWEEN 20 AND 60;

-- & Question-11 Products rated 3 to 5 with a price above ₹20,000.
SELECT "Products rated 3 to 5 with a price above ₹20,000." AS Query_11;

SELECT*FROM product
WHERE (rating BETWEEN 3 AND 5 ) AND price>20000;

-- & Question-12 Electronics or Furniture products manufactured between 2023 and 2025.
SELECT "Electronics or Furniture products manufactured between 2023 and 2025." AS Query_12;

SELECT * FROM product
WHERE category IN ("electronics","furniture") AND year(mfg_date) BETWEEN 2023 AND 2025;

-- & Question-13 Products whose name starts with S.
SELECT "Products whose name starts with S." AS Query_13;

SELECT * FROM product
WHERE product_name LIKE "S%";

-- & Question-14 Products whose name contains phone.
SELECT "Products whose name contains phone." AS Query_14;

SELECT * FROM product
WHERE product_name LIKE "%phone%";


-- & Question-15 Products whose brand ends with a.
SELECT "Products whose brand ends with a." AS Query_15;

SELECT * FROM product
WHERE product_name LIKE "%a";

-- & Question-16 Products from Indore or Pune, priced between ₹20,000 and ₹70,000, rated at least 4.
SELECT "Products from Indore or Pune, priced between ₹20,000 and ₹70,000, rated at least 4." AS Query_16;

SELECT *FROM product
WHERE city IN ("indore","pune") 
AND price BETWEEN 20000 AND 70000
AND rating>=4;

-- & Question-17 Electronics or Furniture products with stock above 10, price below ₹60,000, manufactured after 2022.
SELECT "Electronics or Furniture products with stock above 10, price below ₹60,000, manufactured after 2022." AS Query_17;

SELECT * FROM product
WHERE category IN ("electronics","furniture") 
AND stock>10
AND price<60000
AND year(mfg_date)>2022;


-- & Question-18 Products whose name contains a, price is outside ₹10,000 to ₹50,000, and stock is above 5.
SELECT "Products whose name contains a, price is outside ₹10,000 to ₹50,000, and stock is above 5." AS Query_18;

SELECT * FROM product
WHERE product_name LIKE "%a%" 
AND price NOT BETWEEN 10000 AND 50000
AND stock >5;

-- & Question-19 Products manufactured between 2022 and 2025, in Electronics, Clothing, or Furniture, rated above 3, excluding Mumbai.
SELECT "Products manufactured between 2022 and 2025, in Electronics, Clothing, or Furniture, rated above 3, excluding Mumbai." AS Query_19;


SELECT * FROM product
WHERE year(mfg_date) BETWEEN 2022 AND 2025 
AND category IN ("electronics","clothing","furniture")
AND rating >3
AND city <> "mumbai";



-- & Question-20 Products whose name starts with S or M, excluding Indore and Mumbai, priced between ₹15,000 and ₹80,000, rated at least 4, manufactured after 2023.
SELECT "Products whose name starts with S or M, excluding Indore and Mumbai, priced between ₹15,000 and ₹80,000, rated at least 4, manufactured after 2023." AS Query_20;


SELECT * FROM product
WHERE (product_name LIKE "s%" OR product_name LIKE "m%")
AND city NOT IN ("indore","mumbai")
AND price BETWEEN 15000 AND 80000
AND rating >=4
AND year(mfg_date)>2023;


DROP DATABASE productManagementSystem;