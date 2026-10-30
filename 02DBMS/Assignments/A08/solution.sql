CREATE DATABASE IF NOT EXISTS a08;
use a08;
DROP TABLE if EXISTS sales;

CREATE TABLE if NOT EXISTS sales(
    sale_id INT primary key auto_increment,
    customer_name varchar(50),
    city varchar(30),
    category varchar(30),
    product varchar(50),
    quantity int,
    price decimal(10, 2),
    discount decimal(10,2),
    sale_date date,
    payment_method enum ("UPI", "CARD", "CASH", "NET BANKING"),
    status enum("completed", "pending", "cancelled"),
    customer_type enum("new", "regular", "premium")
);

INSERT ignore into sales
(customer_name, city, category, product, quantity, price, discount, sale_date, payment_method, status, customer_type)
VALUES
('Rahul','Indore','Electronics','Laptop',2,60000,5000,'2026-01-05','Card','Completed','Premium'),
('Priya','Bhopal','Electronics','Mobile',3,25000,3000,'2026-01-07','UPI','Completed','Regular'),
('Amit','Indore','Clothing','Jeans',5,2000,500,'2026-01-10','Cash','Completed','New'),
('Sneha','Mumbai','Beauty','Cream',8,800,400,'2026-01-12','UPI','Completed','Premium'),
('Rohit','Pune','Electronics','Laptop',1,55000,4000,'2026-01-15','Card','Completed','Regular'),
('Neha','Delhi','Clothing','Kurti',6,1800,600,'2026-01-17','UPI','Completed','Premium'),
('Karan','Indore','Sports','Bat',4,3500,700,'2026-01-20','Cash','Completed','Regular'),
('Pooja','Bhopal','Beauty','Lipstick',10,600,300,'2026-01-22','UPI','Completed','New'),
('Vikas','Delhi','Books','SQL Book',7,900,200,'2026-01-25','Net Banking','Completed','Regular'),
('Anjali','Mumbai','Electronics','Watch',3,7000,800,'2026-01-27','Card','Completed','Premium'),
('Saurabh','Pune','Grocery','Rice',12,900,500,'2026-02-01','UPI','Completed','Regular'),
('Riya','Delhi','Electronics','AC',2,45000,5000,'2026-02-03','Card','Completed','Premium'),
('Manish','Indore','Clothing','Shirt',6,1500,300,'2026-02-05','UPI','Completed','New'),
('Komal','Bhopal','Furniture','Chair',3,8000,1000,'2026-02-07','Cash','Completed','Premium'),
('Deepak','Mumbai','Electronics','Speaker',5,3000,500,'2026-02-12','Card','Cancelled','Regular');

-- Q1. Find the total number of completed sales for each city where quantity is greater than 2. Display cities in descending order of sales count.

SELECT city,count(*) AS total_sales
FROM sales
WHERE status="completed" AND quantity>2
GROUP BY city
ORDER BY total_sales desc;




-- Q2. Find the total quantity sold for each category where discount is greater than 300. Display highest quantity first.

SELECT category, SUM(quantity) AS total_quantity
FROM sales
WHERE discount > 300
GROUP BY category
ORDER BY total_quantity DESC;

-- Q3. Find the total sales amount for each city for completed sales only. Display highest-selling city first.

SELECT city,sum(price*quantity) AS total_sales_amt
FROM sales
WHERE status="completed"
GROUP BY city
ORDER BY  total_sales_amt desc;


-- Q4. Find the average product price for each category where quantity is at least 3. Display categories by average price descending.

SELECT category,avg(price) AS avg_price
FROM sales
WHERE quantity>=3
GROUP BY category
ORDER BY avg_price desc;

-- Q5. Find the number of sales for each customer type where the order amount (quantity * price) is greater than 5000. Sort by number of sales descending.

SELECT customer_type,count(*) AS num_sales
FROM sales
WHERE (quantity*price)>5000
GROUP BY customer_type
ORDER BY num_sales DESC;

-- Q6. Find the total discount given for each city for UPI transactions. Display highest discount first.

SELECT city,sum(discount) AS total_dis
FROM sales
WHERE payment_method="upi"
GROUP BY city
ORDER BY total_dis DESC;

-- Q7. Find the total quantity sold through each payment method for completed transactions. Sort by total quantity descending.

SELECT payment_method,sum(quantity) AS total_quantity
FROM sales
WHERE status="completed"
GROUP BY payment_method
ORDER BY total_quantity desc;

-- Q8. Find the average discount for each category where quantity is greater than 4. Display highest average discount first.

SELECT category,avg(discount) AS avg_discount
FROM sales
WHERE quantity>4
GROUP BY category
ORDER BY avg_discount desc;

-- Q9. Find the maximum product price for each city where the status is Completed. Sort by maximum price descending.

SELECT city,max(price) AS max_price
FROM sales
WHERE status="completed"
GROUP BY city
ORDER BY max_price desc;

-- Q10. Find the minimum product price for each category where discount is greater than 300. Sort by minimum price ascending.

SELECT category,min(price) AS min_price
FROM sales
WHERE discount>300
GROUP BY category
ORDER BY min_price asc;



-- Q11. Find cities having more than 2 completed sales. Sort cities by completed sales count descending.

SELECT city ,count(status) AS completed_sales
FROM sales
WHERE status="completed"
GROUP BY city
HAVING completed_sales>2
ORDER BY completed_sales DESC;

-- Q12. Find categories having total quantity greater than 10. Sort by total quantity descending.

SELECT category,sum(quantity) AS total_quantity
FROM sales
GROUP BY category
HAVING total_quantity>10
ORDER BY total_quantity desc;


-- Q13. Find cities having total sales greater than 50,000. Sort by total sales descending.


SELECT city,sum(price*quantity) AS total_sales
FROM sales
GROUP BY city
HAVING total_sales>50000
ORDER BY total_sales desc;

-- Q14. Find customer types having average product price greater than 10,000. Sort by average price descending.

SELECT customer_type,avg(price) AS avg_price
FROM sales
GROUP BY customer_type
having avg_price>10000
ORDER BY avg_price desc;

-- Q15. Find categories having average discount greater than 400. Sort by average discount descending.

SELECT category,avg(discount)AS avg_discount
FROM sales
GROUP BY category
HAVING avg_discount>400
ORDER BY avg_discount desc;


-- Q16. Find payment methods having more than 2 completed transactions. Sort by transaction count descending.

SELECT payment_method,count(status) AS completed_status
FROM sales
WHERE status="completed"
GROUP BY payment_method
HAVING completed_status>2
ORDER BY completed_status desc;

-- Q17. Find cities where the maximum product price is greater than 20,000. Sort by maximum price descending.

SELECT city,max(price) AS max_price
FROM sales
GROUP BY city
HAVING max_price>20000
ORDER BY max_price desc;

-- Q18. Find categories where the minimum product price is less than 2,000. Sort by minimum price ascending.

SELECT category,min(price) AS min_price
FROM sales
GROUP BY category
HAVING min_price>2000
ORDER BY min_price asc;

-- Q19. Find customer types where total discount is greater than 2,000. Sort by total discount descending.

SELECT customer_type,sum(discount) AS total_discount
FROM sales
GROUP BY customer_type
HAVING total_discount>2000
ORDER BY total_discount desc;

-- Q20. Find cities where average quantity per transaction is greater than 4. Sort by average quantity descending.

SELECT city,avg(quantity) AS avg_quantity
FROM sales
GROUP BY city
HAVING avg_quantity>4
ORDER BY avg_quantity desc;


-- Q21. Find each city's total sales for completed UPI transactions where quantity is greater than 2. Display only cities having total sales greater than 10,000.


SELECT city,sum(price*quantity) AS total_sales
FROM sales
WHERE status="completed" AND payment_method="upi" AND quantity>2
GROUP BY city
HAVING total_sales>10000;

-- Q22. Find each category's total quantity for completed transactions where discount is greater than 300. Display only categories having total quantity greater than 5.

SELECT category,sum(quantity) AS total_quantity
FROM sales
WHERE status="completed" AND discount>300
GROUP BY category
HAVING total_quantity>5;

-- Q23. Find each customer type's average price for completed transactions where quantity >= 2. Display only customer types whose average price exceeds 10,000.

SELECT customer_type,avg(price) AS avg_price
FROM sales
WHERE quantity>=2
GROUP BY customer_type
HAVING avg_price >10000;

-- Q24. Find each city's total discount for UPI transactions where quantity > 3. Display cities having total discount greater than 500.

SELECT city,sum(discount) AS total_discount
FROM sales
WHERE payment_method="upi" AND quantity>3
GROUP BY city
HAVING total_discount>500;

-- Q25. Find each category's total sales where payment method is UPI or Card and status is Completed. Display categories having total sales greater than 10,000.

SELECT category,sum(price*quantity) AS total_sales
FROM sales
WHERE payment_method IN ("upi","card") AND status="completed"
GROUP BY category
HAVING total_sales>10000;

-- Q26. Find each city's transaction count for January 2026 completed transactions. Display cities having at least 2 transactions.

SELECT city, COUNT(*) AS transaction_count
FROM sales
WHERE status ='Completed'
AND YEAR(sale_date) = 2026
AND MONTH(sale_date) = 1
GROUP BY city
HAVING transaction_count >= 2;

-- Q27. Find each category's average sales amount where quantity >= 3 and status = Completed. Display categories whose average sales amount is greater than 5,000.

SELECT category,avg(price*quantity) AS avg_sales
FROM sales
WHERE quantity>=3 AND status="completed"
GROUP BY category
HAVING avg_sales>5000;

-- Q28. Find each customer type's maximum price where payment method is Card and status is Completed. Display only customer types whose maximum price exceeds 20,000.

SELECT customer_type,max(price) AS max_price
FROM sales
WHERE payment_method="card" AND status="completed"
GROUP BY customer_type
HAVING max_price>20000;

-- Q29. Find each city's total quantity for Electronics and Clothing products where status is Completed. Display cities having total quantity greater than 5.


SELECT city,sum(quantity) AS total_quantity
FROM sales
WHERE category IN ("electronics","clothing") AND status="completed"
GROUP BY city
HAVING total_quantity>5;

-- Q30. Find each payment method's total sales where status is Completed and discount is greater than 400. Display payment methods having total sales greater than 20,000.

SELECT payment_method,sum(price*quantity) AS total_sales
FROM sales
WHERE status="completed" AND discount>400
GROUP BY payment_method
HAVING total_sales>20000;

-- Q31. Find cities having more than 2 completed transactions and total sales greater than 50,000. Sort by total sales descending.

SELECT
    city,
    COUNT(*) AS completed_transaction,
    SUM(price * quantity) AS total_sales
FROM sales
WHERE status = 'completed'
GROUP BY city
HAVING completed_transaction > 2
   AND total_sales > 50000
ORDER BY total_sales DESC;

-- Q32. Find categories having total quantity greater than 8 and average price greater than 2,000. Sort by total quantity descending.
SELECT category,sum(quantity) AS total_quantity,avg(price) AS avg_price
FROM sales
GROUP BY category
HAVING total_quantity>8 
AND avg_price>2000
ORDER BY total_quantity desc;


-- Q33. Find customer types having more than 2 transactions and total discount greater than 2,000. Sort by total discount descending.

SELECT
    customer_type,
    COUNT(*) AS total_transactions,
    SUM(discount) AS total_discount
FROM sales
GROUP BY customer_type
HAVING total_transactions > 2
   AND total_discount > 2000
ORDER BY total_discount DESC;

-- Q34. Find cities having average quantity greater than 3 and maximum product price greater than 20,000. Sort by average quantity descending.

SELECT city,avg(quantity) avg_quantity,max(price) max_price
FROM sales
GROUP BY city
HAVING avg_quantity>3 AND max_price>2000
ORDER BY avg_quantity desc;

-- Q35. Find categories having more than 2 completed transactions and total sales greater than 20,000. Sort by total sales descending.

SELECT category,count(status) transaction,sum(price*quantity) total_sales
FROM sales
GROUP BY category
HAVING transaction>2 AND total_sales>2000
ORDER BY total_sales desc;

-- Q36. Find payment methods having more than 2 completed transactions and average price greater than 10,000. Sort by average price descending.


SELECT payment_method,count(*) transaction, avg(price) avg_price
FROM sales
GROUP BY payment_method
HAVING transaction>2 AND avg_price>10000
ORDER BY avg_price desc;

-- Q37. Find cities having total quantity greater than 8 and average discount greater than 300. Sort by total quantity descending.

SELECT city,sum(quantity) total_quantity,avg(discount) avg_discount
FROM sales
GROUP BY city
HAVING total_quantity>8 AND avg_discount>300
ORDER BY total_quantity desc;

-- Q38. Find customer types having average price greater than 5,000 and total quantity greater than 8. Sort by total quantity descending.

SELECT customer_type,avg(price) avg_price,sum(quantity) total_quantity
FROM sales
GROUP BY customer_type
HAVING avg_price>5000 AND total_quantity>8
ORDER BY total_quantity desc; 

-- Q39. Find categories having minimum price below 2,000 and maximum price above 20,000. Sort by maximum price descending.

SELECT category,min(price) min_price,max(price) max_price
FROM sales
GROUP BY category
HAVING min_price<2000 AND max_price>20000
ORDER BY max_price desc;

-- Q40. Find cities having total discount greater than 1,000 and total sales greater than 30,000. Sort by total sales descending.

SELECT city,sum(discount) total_discount,sum(price*quantity) total_sales
FROM sales
GROUP BY city
HAVING total_discount>1000 AND total_sales>30000
ORDER BY total_sales desc;


-- Q41. Find the top 3 cities based on total sales, considering only completed transactions with quantity greater than 1 and displaying only cities having more than 1 transaction.

SELECT city,sum(price*quantity) AS total_sales,count(*)AS transaction_count
FROM sales
WHERE status="completed" AND quantity>1
GROUP BY city
HAVING transaction_count>1
ORDER BY total_sales DESC
limit 3;


-- Q42. Find the top 3 categories based on total quantity where discount is greater than 300 and total quantity is greater than 5.

SELECT
    category,
    sum(quantity) total_quantity
FROM sales
WHERE quantity>300
GROUP BY category
HAVING total_quantity>5
ORDER BY total_quantity DESC
limit 3;


-- Q43. Find the top 3 customer types based on average sales amount where status is Completed and transaction count is greater than 1.

SELECT 
    customer_type,
    avg(price*quantity) avg_sales,
    count(*) transaction_count
FROM sales
WHERE status="completed"
GROUP BY customer_type
HAVING transaction_count>1
ORDER BY avg_sales DESC
limit 3;


-- Q44. Find the top 3 cities based on total discount for UPI transactions where status is Completed and total discount is greater than 500.

SELECT
    city,
    sum(discount) total_discount
FROM sales
WHERE status="completed" AND payment_method="upi"
GROUP BY city
HAVING total_discount>500
ORDER BY total_discount DESC
limit 3;

-- Q45. Find the top 3 categories based on total sales where quantity is greater than 2, average price is greater than 1,000, and total sales exceeds 10,000.

SELECT
    category,
    sum(price*quantity) total_sales,
    avg(price) avg_price
FROM sales
WHERE quantity>2
GROUP BY category
HAVING avg_price>1000 AND total_sales>10000
ORDER BY total_sales DESC
limit 3;


-- Q46. Find the top 3 cities based on average order value where status is Completed, total quantity is greater than 5, and transaction count is greater than 1.

SELECT 
    city,
    avg(price*quantity) avg_order,
    sum(quantity) total_quantity,
    count(*) transaction_count
FROM sales
WHERE status="completed"
GROUP BY city
HAVING  total_quantity>5 AND transaction_count>1
ORDER BY avg_order DESC
limit 1;



-- Q47. Find the second-highest city based on total sales after considering only completed transactions and cities having at least 2 transactions.

SELECT
    city,
    sum(price*quantity) total_sales,
    count(*) transaction_count
FROM sales
WHERE status="completed"
GROUP BY city
HAVING transaction_count>=2
ORDER BY total_sales DESC
limit 1 offset 1;


-- Q48. Find the third-highest category based on total quantity where quantity is greater than 2 and total discount exceeds 500.

SELECT 
    category,
    sum(quantity) total_quantity,
    sum(discount) total_discount
FROM sales
WHERE quantity>2
GROUP BY category
HAVING total_quantity>2 AND total_discount>500
ORDER BY total_quantity desc
limit 1 offset 2;

-- Q49. Find the 2nd and 3rd highest customer types based on total sales where status is Completed and average price is greater than 5,000.

SELECT
    customer_type,
    sum(price*quantity) total_sales,
    avg(price) avg_price
FROM sales
WHERE status="completed"
GROUP BY customer_type
HAVING avg_price>5000
ORDER BY total_sales desc
limit 2 offset 1;


-- Q50. Find the top 3 cities where all the following conditions are satisfied:

-- Status is Completed.
-- Payment method is UPI or Card.
-- Quantity is greater than 1.
-- Number of transactions is greater than 1.
-- Total quantity is greater than 5.
-- Total sales is greater than 20,000.

SELECT
    city,
    count(*) transaction_count,
    sum(quantity) total_quantity,
    sum(price*quantity) total_sales
FROM sales
WHERE status="completed" 
    AND payment_method IN ("upi","card") 
    AND quantity>1
GROUP BY city
HAVING 
    total_quantity>5
    AND total_sales>20000
    AND transaction_count>1
limit 3;

