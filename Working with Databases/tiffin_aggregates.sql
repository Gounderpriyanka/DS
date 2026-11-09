-- 1.Add a NULL handling query to 'tiffin_aggregates.sql' that returns avg_rating (`ROUND(AVG(rating), 2)`),
--  avg_rating_null_as_zero (`ROUND(AVG(COALESCE(rating, 0)), 2)`) and 
-- unrated_orders (orders where `rating IS NULL`). Run it and confirm unrated_orders equals
-- total_orders minus rated_orders from your first query.
-- Hint: `COUNT(*)` counts rows, but `COUNT(column)` skips NULLs.

create database aggregates;
use aggregates;

create table ratings(
	order_id int primary key,
    customer varchar(50),
    rating int
);

insert into ratings values
(1,"Priya",5),
(2,"Rahul",4),
(3,"Neha",null),
(4,"Amit",3),
(5,"Sneha",null),
(6,"Raj",5),
(7,"Pooja",4),
(8,"Karan",null),
(9,"Meera",2),
(10,"Dev",5);


select 
count(*) - count(rating) as unrated_orders,
ROUND(AVG(rating), 2) as avg_rating ,
ROUND(AVG(COALESCE(rating, 0)), 2) as avg_rating_null_as_zero
from ratings ;

-- Task 2.Finish 'tiffin_aggregates.sql' with a business report for Jain meals ordered in February 2026
--  only: total orders, revenue, average rating and slowest delivery, using WHERE with BETWEEN and 
-- the same aggregate functions, with a clear alias on every column. Run the whole file top to bottom.
--  Constraint: Do not use GROUP BY; it is taught in the next session.

alter table ratings 
add column 	meal_type varchar(50),
add column order_date date,
add column amount int,
add column delivery_minutes int;

select * from ratings;

set sql_Safe_updates = 0;
UPDATE ratings
SET 
    meal_type = CASE order_id
        WHEN 1 THEN 'Jain'
        WHEN 2 THEN 'Punjabi'
        WHEN 3 THEN 'Jain'
        WHEN 4 THEN 'Jain'
        WHEN 5 THEN 'Gujarati'
        WHEN 6 THEN 'Jain'
        WHEN 7 THEN 'Jain'
        WHEN 8 THEN 'Punjabi'
        WHEN 9 THEN 'Jain'
        WHEN 10 THEN 'Jain'
    END,

    order_date = CASE order_id
        WHEN 1 THEN '2026-02-02'
        WHEN 2 THEN '2026-02-03'
        WHEN 3 THEN '2026-02-05'
        WHEN 4 THEN '2026-02-10'
        WHEN 5 THEN '2026-02-12'
        WHEN 6 THEN '2026-02-15'
        WHEN 7 THEN '2026-02-20'
        WHEN 8 THEN '2026-02-25'
        WHEN 9 THEN '2026-03-02'
        WHEN 10 THEN '2026-02-28'
    END,

    amount = CASE order_id
        WHEN 1 THEN 120
        WHEN 2 THEN 180
        WHEN 3 THEN 150
        WHEN 4 THEN 200
        WHEN 5 THEN 100
        WHEN 6 THEN 130
        WHEN 7 THEN 160
        WHEN 8 THEN 220
        WHEN 9 THEN 140
        WHEN 10 THEN 110
    END,

    delivery_minutes = CASE order_id
        WHEN 1 THEN 25
        WHEN 2 THEN 35
        WHEN 3 THEN 40
        WHEN 4 THEN 55
        WHEN 5 THEN 30
        WHEN 6 THEN 65
        WHEN 7 THEN 45
        WHEN 8 THEN 50
        WHEN 9 THEN 20
        WHEN 10 THEN 70
    END;
set sql_safe_updates = 1;


