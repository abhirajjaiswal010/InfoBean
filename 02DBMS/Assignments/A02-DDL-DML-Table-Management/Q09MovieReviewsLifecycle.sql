
-- QNO 9: Movie Reviews Table Lifecycle

-- Initial Table Creation
-- Create a table and insert 3 sample movie reviews.

CREATE TABLE IF NOT EXISTS creation (
    review_id INT UNIQUE,
    movie_title VARCHAR(150),
    reviewer_name VARCHAR(100),
    rating DECIMAL(2,1),
    review_text TEXT
);

INSERT IGNORE INTO creation
    (review_id, movie_title, reviewer_name, rating, review_text)
VALUES
    (1, '3 Idiots', 'Aarav Sharma', 4.5,
     'An inspiring movie about friendship and education.'),
    (2, 'Dangal', 'Priya Verma', 4.8,
     'A powerful story with excellent performances.'),
    (3, 'Inception', 'Rahul Patel', 4.7,
     'A mind-bending movie with a brilliant storyline.');

DESC creation;
SELECT * FROM creation;


-- Step 1: Add More Columns
-- Add review_date, platform, and likes.

ALTER TABLE creation
    ADD COLUMN review_date DATE,
    ADD COLUMN platform VARCHAR(50),
    ADD COLUMN likes INT;

-- Insert 2 more reviews with values for the new columns.

INSERT IGNORE INTO creation
    (review_id, movie_title, reviewer_name, rating, review_text,
     review_date, platform, likes)
VALUES
    (4, 'Interstellar', 'Sneha Jain', 4.9,
     'An amazing science fiction movie with emotional depth.',
     '2026-10-14', 'IMDb', 250),
    (5, 'The Dark Knight', 'Arjun Gupta', 4.8,
     'An outstanding superhero movie with a compelling villain.',
     '2026-10-14', 'Rotten Tomatoes', 180);

DESC creation;
SELECT * FROM creation;


-- Step 2: Rename a Column
-- Rename reviewer_name to critic_name.

ALTER TABLE creation
    RENAME COLUMN reviewer_name TO critic_name;

DESC creation;


-- Step 3: Modify Column Types
-- Modify rating to DECIMAL(3,1).
-- Modify movie_title to VARCHAR(200).

ALTER TABLE creation
    MODIFY COLUMN rating DECIMAL(3,1),
    MODIFY COLUMN movie_title VARCHAR(200);

DESC creation;


-- Step 4: Drop an Unnecessary Column
-- Drop the likes column.

ALTER TABLE creation
    DROP COLUMN likes;

DESC creation;


-- Step 5: Truncate the Table
-- Remove all records while retaining the table structure.

TRUNCATE TABLE creation;

SELECT * FROM creation;
DESC creation;


-- Step 6: Rename the Table
-- Rename creation to archived_reviews.

RENAME TABLE creation TO archived_reviews;

SHOW TABLES LIKE 'archived_reviews';
DESC archived_reviews;


-- Step 7: Drop the Table
-- Permanently remove the archived_reviews table.

DROP TABLE archived_reviews;

SHOW TABLES LIKE 'archived_reviews';

