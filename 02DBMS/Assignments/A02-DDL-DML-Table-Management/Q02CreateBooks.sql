-- QNO 2: Create and Populate Books Table
-- Columns:
-- book_id INT
-- title VARCHAR(150)
-- author VARCHAR(100)
-- genre VARCHAR(50)
-- publication_year INT
-- price DECIMAL(6,2)
-- publisher VARCHAR(100)
-- Task: Insert 4 book records.


CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY,
    title VARCHAR(150),
    author VARCHAR(100),
    genre VARCHAR(50),
    publication_year INT,
    price DECIMAL(6,2),
    publisher VARCHAR(100)
);

INSERT IGNORE INTO books
VALUES
    (1, 'Atomic Habits', 'James Clear', 'Self-Help', 2018, 499.00, 'Penguin Random House'),
    (2, 'The Alchemist', 'Paulo Coelho', 'Fiction', 1988, 299.00, 'HarperOne'),
    (3, 'Clean Code', 'Robert C. Martin', 'Programming', 2008, 650.00, 'Prentice Hall'),
    (4, 'Deep Work', 'Cal Newport', 'Productivity', 2016, 399.00, 'Grand Central Publishing');

SELECT * FROM books;
