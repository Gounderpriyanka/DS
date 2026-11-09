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

