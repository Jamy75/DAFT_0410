-- LAB 19 (9 questions)

SELECT * FROM olist.prod_cat_price;
-- Question 1
SELECT Max(price) from olist.prod_cat_price;
SELECT MIN(price) from olist.prod_cat_price;
-- Question 2 From the `order_items` table, what is range of the shipping_limit_date of the orders?
SELECT MIN(shipping_limit_date) AS earliest_date, MAX(shipping_limit_date) AS latest_date FROM order_items;
-- 3. From the `customers` table, find the states with the greatest number of customers.
SELECT * FROM olist.customers;
SELECT Max(customer_state) from olist.customers;
-- 4. From the `customers` table, within the state with the greatest number of customers
-- find the cities with the greatest number of customers.
FROM customers
SELECT 

-- 5. From the `closed_deals` table, how many distinct business segments are there (not including null)?
SELECT DISTINCT business_segment FROM closed_deals;
-- 6. From the `closed_deals` table, sum the declared_monthly_revenue for duplicate row values in business_segment and 
-- find the 3 business segments with the highest declared monthly revenue (of those that declared revenue).
