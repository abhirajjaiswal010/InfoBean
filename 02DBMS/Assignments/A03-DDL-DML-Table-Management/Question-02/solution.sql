CREATE DATABASE if NOT EXISTS libraryManagement;
use libraryManagement;
CREATE TABLE  if NOT EXISTS books (
    book_id INT unsigned AUTO_INCREMENT PRIMARY KEY,
    book_title VARCHAR(100) NOT NULL,
    author_name VARCHAR(100) NOT NULL,
    isbn_number VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    number_of_copies INT UNSIGNED NOT NULL DEFAULT 0,
    book_category ENUM(
        'FICTION',
        'SCIENCE',
        'TECHNOLOGY',
        'HISTORY',
        'EDUCATION',
        'FANTASY',
        'BIOGRAPHY',
        'OTHER'
    ) NOT NULL DEFAULT 'OTHER',
    publication_date DATE,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    description MEDIUMTEXT
);
CREATE TABLE if NOT EXISTS  student(
    student_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    student_name varchar(100) NOT null,
    enrollment_number varchar(30) unique NOT null,
    age TINYINT unsigned,
    gender ENUM('MALE', 'FEMALE', 'OTHER'),
    dob date,
    contact_number varchar(15),
    email varchar(100) unique,
    is_active BOOLEAN NOT NULL DEFAULT true,
    registration_date DATE NOT NULL default(current_date)
);
CREATE TABLE if NOT EXISTS  book_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    book_id INT,
    issue_date DATE,
    expected_return_date DATE,
    actual_return_date DATE,
    fine_amount DECIMAL(8, 2),
    is_returned BOOLEAN,
    remarks VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- record
INSERT ignore INTO books (
        book_title,
        author_name,
        isbn_number,
        price,
        number_of_copies,
        book_category,
        publication_date,
        is_available,
        description
    )
VALUES (
        'The Alchemist',
        'Paulo Coelho',
        '9780061122415',
        399.00,
        5,
        'FICTION',
        '1988-01-01',
        TRUE,
        'A story about dreams and destiny.'
    ),
    (
        'Brief History of Time',
        'Stephen Hawking',
        '9780553380163',
        450.00,
        3,
        'SCIENCE',
        '1988-04-01',
        TRUE,
        'An introduction to cosmology.'
    ),
    (
        'Clean Code',
        'Robert C. Martin',
        '9780132350884',
        650.00,
        4,
        'TECHNOLOGY',
        '2008-08-01',
        TRUE,
        'A guide to writing maintainable code.'
    ),
    (
        'Wings of Fire',
        'A. P. J. Abdul Kalam',
        '9788173711466',
        299.00,
        6,
        'BIOGRAPHY',
        '1999-01-01',
        TRUE,
        'An autobiography of A. P. J. Abdul Kalam.'
    ),
    (
        'The Discovery of India',
        'Jawaharlal Nehru',
        '9780143031031',
        499.00,
        2,
        'HISTORY',
        '1946-01-01',
        TRUE,
        'A book exploring Indian history and culture.'
    );

INSERT ignore INTO student (
        student_name,
        enrollment_number,
        age,
        gender,
        dob,
        contact_number,
        email,
        is_active,
        registration_date
    )
VALUES (
        'Rahul Sharma',
        'ENR2026001',
        21,
        'MALE',
        '2005-02-15',
        '9876543210',
        'rahul@example.com',
        TRUE,
        '2026-06-10'
    ),
    (
        'Priya Verma',
        'ENR2026002',
        20,
        'FEMALE',
        '2006-04-20',
        '9876543211',
        'priya@example.com',
        TRUE,
        '2026-06-11'
    ),
    (
        'Aman Patel',
        'ENR2026003',
        22,
        'MALE',
        '2004-08-12',
        '9876543212',
        'aman@example.com',
        TRUE,
        '2026-06-12'
    ),
    (
        'Sneha Gupta',
        'ENR2026004',
        19,
        'FEMALE',
        '2007-01-25',
        '9876543213',
        'sneha@example.com',
        TRUE,
        '2026-06-13'
    ),
    (
        'Arjun Singh',
        'ENR2026005',
        21,
        'MALE',
        '2005-05-30',
        '9876543214',
        'arjun@example.com',
        FALSE,
        '2026-06-14'
    );


INSERT ignore INTO book_transactions (
        student_id,
        book_id,
        issue_date,
        expected_return_date,
        actual_return_date,
        fine_amount,
        is_returned,
        remarks
    )
VALUES (
        1,
        1,
        '2026-09-01',
        '2026-09-15',
        '2026-09-12',
        0.00,
        TRUE,
        'Returned early'
    ),
    (
        2,
        2,
        '2026-09-05',
        '2026-09-19',
        '2026-09-22',
        30.00,
        TRUE,
        'Returned late'
    ),
    (
        3,
        3,
        '2026-09-10',
        '2026-09-24',
        '2026-09-24',
        0.00,
        TRUE,
        'Returned on time'
    ),
    (
        4,
        4,
        '2026-10-05',
        '2026-10-19',
        NULL,
        0.00,
        FALSE,
        'Book currently issued'
    ),
    (
        5,
        5,
        '2026-10-07',
        '2026-10-21',
        NULL,
        0.00,
        FALSE,
        'Return pending'
    );

SELECT * FROM books;
SELECT * FROM student;
SELECT * FROM book_transactions;

SHOW DATABASES;
SHOW TABLES;

DESC books;
DESC students;
DESC book_transactions;

DROP DATABASE IF EXISTS libraryManagement;


