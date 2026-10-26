-- Task 1
-- 1.Create a SQL query using a subquery in the WHERE clause to find all restaurants from a 'Restaurants'
-- table whose average rating is higher than the average rating of all restaurants in the city.

use foodie_app;

select * from restaurants;

select distinct city,avg(rating) as avg_rating
from restaurants
group by city;

SELECT r.id, r.name, r.city, AVG(r.rating) AS avg_rating
FROM Restaurants AS r
GROUP BY r.id, r.name, r.city
HAVING AVG(r.rating) > (
    SELECT AVG(r2.rating)
    FROM Restaurants AS r2
    WHERE r2.city = r.city
);