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


create table tifin (
	order_id int primary key,
    area varchar(50),
    quantity int,
    price_inr int,
    rating int,
    delivery_minutes int
);

INSERT INTO tifin
(order_id, area, quantity, price_inr, rating, delivery_minutes)
VALUES
(1, 'Maninagar', 2, 120, 5, 45),
(2, 'Maninagar', 1, 120, 4, 50),
(3, 'Maninagar', 3, 120, 5, 42),
(4, 'Satellite', 2, 150, 4, 55),
(5, 'Satellite', 1, 150, 5, 48),
(6, 'Satellite', 2, 150, 4, 45),
(7, 'Bopal', 3, 100, 5, 35),
(8, 'Bopal', 2, 100, 4, 38),
(9, 'Bopal', 1, 100, 5, 40),
(10, 'Vastrapur', 2, 180, 4, 52),
(11, 'Vastrapur', 1, 180, 5, 46),
(12, 'Vastrapur', 3, 180, 4, 50);

select area,count(*) as orders,avg(delivery_minutes)
from tifin
group by area
having COUNT(*) >= 3 and 
avg(delivery_minutes)>40;

-- 4.Finish 'tiffin_groups.sql' with a report named february_area_report:
-- for orders dated in February 2026 only (filtered with WHERE), 
-- return per-area orders and revenue_inr, keep only areas 
-- whose revenue_inr is above 5000 using HAVING (adjust the amount so 2 to 6 areas remain)
-- , and sort by revenue_inr descending. Run the file top to bottom.
-- Hint: WHERE filters rows before grouping; HAVING filters groups
--  after the aggregates are calculated.

create table task4(
	order_id int primary key,
    area varchar(50),
    quantity int,
    price_inr int,
    order_date date
);

INSERT INTO task4
(order_id, area, quantity, price_inr, order_date)
VALUES
(1, 'Maninagar', 10, 150, '2026-02-03'),
(2, 'Maninagar', 8, 200, '2026-02-08'),
(3, 'Maninagar', 6, 180, '2026-02-15'),

(4, 'Satellite', 12, 200, '2026-02-05'),
(5, 'Satellite', 10, 250, '2026-02-12'),
(6, 'Satellite', 8, 200, '2026-02-20'),

(7, 'Bopal', 10, 150, '2026-02-04'),
(8, 'Bopal', 12, 180, '2026-02-10'),
(9, 'Bopal', 10, 200, '2026-02-18'),

(10, 'Vastrapur', 10, 200, '2026-02-06'),
(11, 'Vastrapur', 8, 250, '2026-02-14'),
(12, 'Vastrapur', 6, 200, '2026-02-25'),

(13, 'Chandkheda', 5, 120, '2026-02-07'),
(14, 'Chandkheda', 6, 150, '2026-02-16'),

(15, 'Thaltej', 10, 200, '2026-02-09'),
(16, 'Thaltej', 8, 250, '2026-02-21'),

(17, 'Gota', 10, 180, '2026-02-11'),
(18, 'Gota', 8, 200, '2026-02-23'),

(19, 'Maninagar', 5, 100, '2026-01-20'),
(20, 'Satellite', 3, 150, '2026-03-05');

select * from task4;

select area,count(*) as orders,
 sum(quantity*price_inr) as Revenue_inr
from task4
where order_date between '2026-02-01' and '2026-02-28'
group by area
having revenue_inr > 5000
order by revenue_inr desc;


