
-- Task 1
use music_streaming_app;

create table MusicPlaylist(
	id int primary	key,
    song_name varchar(100),
    artist varchar(100),
    genre varchar(100),
    duration int 
);

insert into MusicPlaylist values
(1,"Believer","Imagine Dragons","Pop Rock",204),
(2,"Perfect","Ed Sheeran","Pop",263),
(3,"Counting Stars","OneRepublic","Pop Rock",257),
(4,"Shape of you","Ed Sheeran","Pop",234),
(5,"Faded","Alan Walker","Electronic",212);

Select * from MusicPlaylist;

-- Task 2

-- Task 3
use foodie_app;

create table FoodOrders(
	id int primary key,
    restaurant varchar(100),
    food_item varchar(100),
    order_date date
);

insert into FoodOrders value
(1,"Domino's","Pizza","2026-09-10");

insert into FoodOrders values
(2,"McDonald's","Burger","2026-09-11"),
(3,"Domino's","Pasta","2026-09-12"),
(4,"Subway","Sandwich","2026-09-13"),
(5,"McDonald's","Fries","2026-09-14"),
(6,"Domino's","Garlic Bread","2026-09-15"),
(7,"subway","Wrap","2026-09-16");

select * from Foodorders;

-- Task 4
Select food_item as Dish,order_date as Date_Ordered
from foodorders

-- Task 5
