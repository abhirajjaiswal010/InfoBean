-- QNO 7: Create and Populate Products Table
-- Columns:
-- product_id INT
-- product_name VARCHAR(100)
-- category VARCHAR(50)
-- price DECIMAL(7,2)
-- stock_quantity INT
-- supplier_name VARCHAR(100)
-- manufacture_date DATE
-- expiry_date DATE
-- Task: Insert 6 products, some with expiry dates and some without.


-- QNO 7: Create and Populate Products Table

CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(7,2),
    stock_quantity INT,
    supplier_name VARCHAR(100),
    manufacture_date DATE,
    expiry_date DATE
);

INSERT IGNORE INTO products
    
VALUES
    (1, 'Amul Milk', 'Dairy',  30.00,  50, 'Amul Dairy',
     '2026-10-01', '2026-10-15'),

    (2, 'Whole Wheat Bread', 'Bakery', 45.00, 30, 'Fresh Bakery',
     '2026-10-10', '2026-10-17'),

    (3, 'Laptop', 'Electronics', 55000.00, 10, 'Dell India',
     '2026-08-15', NULL),

    (4, 'Office Chair', 'Furniture', 4500.00, 15, 'Comfort Furnishings',
     '2026-07-20', NULL),

    (5, 'Orange Juice', 'Beverages', 120.00, 25, 'Tropicana',
     '2026-10-05', '2027-01-05'),

    (6, 'Shampoo', 'Personal Care', 180.00, 40, 'Hindustan Unilever',
     '2026-09-01', '2028-08-31');


SELECT * FROM products;
