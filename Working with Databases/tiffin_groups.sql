create database group_s;

-- 1.Create 'tiffin_groups.sql' with a query on `tiffin_orders` that returns one row per area with orders (COUNT),
--  revenue_inr (SUM of quantity * price_inr) and avg_rating, sorted by revenue_inr descending. 
-- Confirm it returns exactly 8 rows. Hint: Every non-aggregated column in SELECT must also be in GROUP BY,
-- or PostgreSQL will refuse the query.

use group_s;
create table tiffin_orders(
	order_id int primary key,
    area varchar(50),
	quantity int,
    price_inr int,
    rating int 
);

INSERT INTO tiffin_orders
(order_id, area, quantity, price_inr, rating)
VALUES
(1, 'Maninagar', 2, 120, 5),
(2, 'Satellite', 1, 150, 4),
(3, 'Bopal', 3, 100, 5),
(4, 'Vastrapur', 2, 180, 4),
(5, 'Maninagar', 1, 120, 4),
(6, 'Satellite', 2, 150, 5),
(7, 'Chandkheda', 3, 90, 4),
(8, 'Bopal', 2, 100, 3),
(9, 'Vastrapur', 1, 180, 5),
(10, 'Navrangpura', 2, 200, 5),
(11, 'Chandkheda', 1, 90, 3),
(12, 'Thaltej', 2, 160, 4),
(13, 'Navrangpura', 1, 200, 4),
(14, 'Thaltej', 1, 160, 5),
(15, 'Gota', 3, 110, 4),
(16, 'Gota', 1, 110, 5);

select * from tiffin_orders;

select area,
count(*) as Orders,
sum(quantity * price_inr) as Revenue_inr,
avg(rating) as avg_rating
from tiffin_orders
group by area
order by  Revenue_inr desc;

-- 2.Add a query to 'tiffin_groups.sql' that groups orders by area and meal_type and returns orders,
-- total_quantity and avg_delivery_minutes rounded to 1 decimal, sorted by area then meal_type. 
-- Run it and write the row count in a comment; it should be at most 32.

create table tiffin_orders_with_meal_type(
	order_id int primary key,
    area varchar(50),
    meal_type varchar(50),
    quantity int,
    delivery_minutes int 
);

INSERT INTO tiffin_orders_with_meal_type
(order_id, area, meal_type, quantity, delivery_minutes)
VALUES
(1, 'Maninagar', 'Lunch', 2, 30),
(2, 'Maninagar', 'Dinner', 1, 40),
(3, 'Satellite', 'Lunch', 1, 25),
(4, 'Satellite', 'Dinner', 2, 35),
(5, 'Bopal', 'Lunch', 3, 45),
(6, 'Bopal', 'Dinner', 2, 40),
(7, 'Vastrapur', 'Lunch', 2, 30),
(8, 'Vastrapur', 'Dinner', 1, 35),
(9, 'Chandkheda', 'Lunch', 3, 50),
(10, 'Chandkheda', 'Dinner', 1, 45),
(11, 'Navrangpura', 'Lunch', 2, 25),
(12, 'Navrangpura', 'Dinner', 1, 30),
(13, 'Thaltej', 'Lunch', 2, 35),
(14, 'Thaltej', 'Dinner', 1, 40),
(15, 'Gota', 'Lunch', 3, 45),
(16, 'Gota', 'Dinner', 1, 50);


select area,
meal_type,
count(*) as Orders,
sum(quantity) as Total_Quantity,
round(avg(delivery_minutes),1) as Avg_delivery_minutes
from tiffin_orders_with_meal_type
group by area, meal_type
order by area, meal_type; -- row count 16

-- 3.Add a HAVING query to 'tiffin_groups.sql' that lists areas with at least 30 orders and 
-- an average delivery_minutes above 40. If it returns fewer than 2 or more than 5 areas, 
-- change the two thresholds until it returns between 2 and 5, and keep the final values with the
-- area names as a comment.
