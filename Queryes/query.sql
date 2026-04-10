-- Create a new database named Books
CREATE DATABASE Books;

-- Use the Books database
USE Books;

-- Count total number of records in the books table
SELECT COUNT(*) FROM books;

-- Count number of books in each category
SELECT Category, COUNT(name) AS books_count
FROM books
GROUP BY Category;

-- Get top 5 categories with highest total price
SELECT Category, ROUND(SUM(price), 0) AS total_price
FROM books
GROUP BY Category
ORDER BY total_price DESC
LIMIT 5;

-- Get top 5 categories with highest total rating
SELECT Category, ROUND(SUM(Rating), 0) AS total_rating
FROM books
GROUP BY Category
ORDER BY total_rating DESC
LIMIT 5;

-- Find books that are NOT in stock
SELECT name
FROM books
WHERE Availability <> 'In stock';

-- Get top 5 most expensive books (by total price grouped by category - logically odd but kept as per your query)
SELECT name, ROUND(SUM(price), 0) AS total_price
FROM books
GROUP BY name
ORDER BY total_price DESC
LIMIT 5;

-- Get top 5 books with highest ratings (grouped by category - logically needs fix but kept as is)
SELECT name, ROUND(SUM(Rating), 0) AS total_rating
FROM books
GROUP BY Category
ORDER BY total_rating DESC
LIMIT 5;

-- Get average rating of books in each category
SELECT Category, ROUND(AVG(rating), 1) AS avg_rating
FROM books
GROUP BY Category;

