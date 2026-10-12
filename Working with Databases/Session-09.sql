use products;
-- Task 1
create table Restaurants
( 
	id int primary key,
    name varchar(50) ,
    city varchar(50)
);
insert into restaurants values
(1,"Spice Garden","Mumbai"),
(2,"The Pasta Room","Pune"),
(3,"Green Bowl","Bengaluru"),
(4,"Cafe Empty Plate","Delhi");

create table Dishes
(
	id int primary key,
    restaurant_id int,
    foreign key (restaurant_id) references restaurants(id),
    dish_name varchar(50),
    price int
    
);

insert into Dishes values
(1,1,"Paneer Tikka",280),
(2,1,"Butter Naan",60),
(3,2,"Alfredo Pasta",320),
(4,2,"Garlic Bread",150),
(5,3,"Buddha Bowl",260),
(6,3,"Mango Smoothie",180),
(7,1,"Test dish",100);

insert into Dishes values
(8,1,null,00),
(9,2,null,00);
 
select * from dishes;

select * from restaurants;

-- 2.Write an SQL INNER JOIN query to display each dish along with its restaurant name and city, 
-- similar to how Zomato shows dish details with the restaurant info.

select r.name,r.city,dishes.dish_name as name
from restaurants r
inner join dishes on r.id = dishes.restaurant_id;

-- 3.Write an SQL LEFT JOIN query to list all restaurants and their dishes, showing restaurants even 
-- if they currently have no dishes on the menu.Use LEFT JOIN so restaurants without dishes still 
-- appear in the results with NULL for dish columns.
select r.name,d.dish_name
from restaurants r
left join dishes d
on r.id = d.restaurant_id;

-- 4.Write an SQL RIGHT JOIN query to display all dishes and their restaurant names, 
-- including any dishes that might not be linked to a restaurant (simulate a data error 
-- where a dish has a restaurant_id that doesn't match any restaurant).

select r.name,d.dish_name
from dishes d 
right join restaurants r
on r.id = d.restaurant_id;

-- 5.Given this scenario: You want to show a list of all playlists and the songs inside them, 
-- like Spotify. Explain which JOIN type (INNER, LEFT, or RIGHT) you would use to show all playlists,
-- even if some are empty, and write the SQL query for it.

use music_streaming_app;

create table spotify(
	playlist_id int primary key,
    playlist_name varchar(40));
    
INSERT INTO spotify VALUES
(1, 'Top Hits'),
(2, 'Workout Mix'),
(3, 'Chill Vibes'),
(4, 'Road Trip'),
(5, 'Empty Playlist');
    
create table spotify2(
	song_id int primary key,
    playlist_id int,
    foreign key (playlist_id) references spotify(playlist_id),
    song_name varchar(50),
    artist varchar(50)
);


INSERT INTO Spotify2 VALUES
(1, 1, 'Perfect', 'Ed Sheeran'),
(2, 1, 'Believer', 'Imagine Dragons'),
(3, 2, 'Faded', 'Alan Walker'),
(4, 2, 'Closer', 'The Chainsmokers'),
(5, 3, 'Heat Waves', 'Glass Animals'),
(6, 4, 'Blinding Lights', 'The Weeknd');

select s.playlist_name




