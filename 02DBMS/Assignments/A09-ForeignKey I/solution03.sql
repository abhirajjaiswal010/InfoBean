use Assign03;

CREATE TABLE if NOT EXISTS author
(
    author_id INT primary key AUTO_INCREMENT  ,
    author_name varchar(100) not NULL unique
);

CREATE TABLE if NOT EXISTS book
(
    book_id INT primary key auto_increment,
    book_title varchar(100) NOT NULL UNIQUE,
    author_id INT ,

    constraint fk_author_book
    FOREIGN key (author_id)
    REFERENCES author(author_id)

    on DELETE SET NULL
);

INSERT IGNORE INTO author (author_name)
VALUES
('J.K. Rowling'),
('Chetan Bhagat'),
('R.K. Narayan');

INSERT IGNORE INTO book (book_title, author_id)
VALUES
('Harry Potter and the Philosopher Stone', 1),
('Harry Potter and the Chamber of Secrets', 1),
('Five Point Someone', 2),
('The 3 Mistakes of My Life', 2),
('Malgudi Days', 3);

SELECT * FROM author;
SELECT * FROM book;


-- Delete an author and verify that their books remain in the Books table with AuthorID set to NULL.

DELETE FROM author
WHERE author_id=1;


-- Update the author of a book to a new author.

INSERT into author(author_name)
VALUES("ruskin Bond");

UPDATE book
set author_id=4
WHERE book_id=1;