CREATE DATABASE library;

USE library;

CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    price DECIMAL(10,2)
);
INSERT INTO books (id, title, author, price)
VALUES
(1, 'Python Basics', 'Ali', 450),
(2, 'Learn SQL', 'Ahmed', 700),
(3, 'Java Programming', 'Sara', 900),
(4, 'Web Development', 'Ali', 550),
(5, 'Data Science', 'Ahmed', 1200),
(6, 'HTML CSS', 'Sara', 350),
(7, 'Machine Learning', 'Ali', 1500),
(8, 'Computer Networks', 'Ahmed', 800);

SELECT * from books


SELECT * FROM books
WHERE price > 500;

SELECT * FROM books
ORDER BY price DESC;


SELECT * FROM books
ORDER BY price ASC;


select author ,count(*)as Total_books
from books
group by author

update books
set price = 1500
where id=5;