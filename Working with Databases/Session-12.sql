-- Task 1.Create a CTE using the WITH clause to select all products with a rating above 4.5 from a
-- 'Products' table, similar to how Flipkart or Myntra might highlight top-rated items.

use foodie_app;

select * from restaurants;
with Product_rating as(
	select * 
    from restaurants
    where rating>4.5
)
select * from product_rating;

-- Task 2.Rewrite a query that finds all restaurants in 'Ahmedabad' with delivery charges 
-- under 50 from a 'Restaurants' table, first using a subquery and then using a CTE. 
-- Compare both queries for readability.Focus on making the CTE version cleaner and easier to understand.

create database CTE;
use cte;
CREATE TABLE Restaurants (
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(100),
    city VARCHAR(100),
    delivery_charge DECIMAL(6, 2)
);

INSERT INTO Restaurants (restaurant_id, restaurant_name, city, delivery_charge) VALUES
(1, 'Spice Route', 'Ahmedabad', 35.00),
(2, 'Green Leaf Cafe', 'Ahmedabad', 45.00),
(3, 'Pizza Corner', 'Ahmedabad', 55.00),
(4, 'Royal Thali', 'Ahmedabad', 0.00),
(5, 'South Kitchen', 'Surat', 30.00),
(6, 'Urban Bites', 'Ahmedabad', 49.50);


-- subquery method
select r.restaurant_name,r.city,r.delivery_charge
from restaurants r
where r.city = "Ahmedabad" and r.delivery_charge in(
	select r2.delivery_charge
    from restaurants r2
    where r2.delivery_charge<50);
    
-- cte method
with Display_Ahmedabad_restaurant_under_50_deliverycharge as(
select r.restaurant_name,r.city,r.delivery_charge
from restaurants r
where r.city = "Ahmedabad" and r.delivery_charge<50
)

select * from Display_Ahmedabad_restaurant_under_50_deliverycharge;


-- 3.Using two CTEs in a single query, find the top 3 most-followed users and the top 3 most-liked
-- posts from a 'Users' and 'Posts' table (think Instagram-style data). Output both lists in the same result set.



CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    followers_count INT
);

INSERT INTO Users (user_id, username, followers_count) VALUES
(1, 'maya_foodie', 2450),
(2, 'arjun_travels', 1875),
(3, 'nisha_creates', 3200),
(4, 'dev_codes', 980),
(5, 'riya_style', 1540),
(6, 'kabir_music', 760),
(7, 'sana_art', 1100),
(8, 'veer_fitness', 430);


CREATE TABLE Posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    caption VARCHAR(255),
    likes_count INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Posts (post_id, user_id, caption, likes_count) VALUES
(101, 1, 'Weekend food trail', 1250),
(102, 3, 'New artwork', 2100),
(103, 2, 'Sunset by the sea', 980),
(104, 5, 'Outfit of the day', 1750),
(105, 1, 'Homemade pasta', 1430),
(106, 7, 'Watercolor practice', 870),
(107, 3, 'Behind the scenes', 1600),
(108, 4, 'A useful coding tip', 740);

with top_3_most_followed as (
	select * from users
    order by followers_count desc
    limit 3
),top_3_most_liked as (
select * 
from posts
order by likes_count desc
limit 3
),
top


    
                                                                                                                      