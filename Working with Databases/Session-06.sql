-- Task 1
create database products;

use products;
create table product(
	id int primary key,
    Product_name varchar(100),
    Price int 
);

insert into product values
(1,"Wireless Mouse",599),
(2,"Keyboard",899),
(3,"Headphones",1499),
(4,"Laptop Bag",799),
(5,"Smart Watch",2499),
(6,"Bluetooth Speaker",1799),
(7,"USB Cable",299),
(8,"Power Bank",1299);

select *  from product;

select product_name,price
from product
order by price asc;

-- Task 2
select product_name,price
from product
order by price desc
limit 5;

-- Task 3
create table Movies(
	movie_id int primary key,
    title varchar(100),
    release_year date,
    rating decimal(2,1)
);

alter table movies
modify column release_year int;

insert into movies value
(1,"Inception",2010,8.8);

insert into movies values
(2,"Interstellar",2014,8.7),
(3,"Dune",2021,8.0),
(4,"Oppenheimer",2023,8.6),
(5,"Avatar 2",2022,7.6),
(6,"The Batman",2022,7.8),
(7,"Avengers Endgame",2019,8.4),
(8,"Dune Part Two",2024,8.5);

select title,release_year
from movies
order by release_year desc;

select title,rating
from movies
order by rating desc;

-- Task 4
use foodie_app;
select * from restaurants ;

select name ,cuisine,rating
from restaurants
order by name asc
limit 10;

-- Task 5
use music_streaming_app;

create table songs(
	song_id int primary key,
    song_name varchar(100),
    artist varchar(100),
    play_count int,
    added_date date
);

insert into songs value
(1,"Perfect","Ed Sheeran",950000,"2026-01-15");

insert into songs values
(2,"Shape of You","Ed Sheeran",1200000,"2026-03-10"),
(3,"Believer","Imagine Dragons",1100000,"2026-02-20"),
(4,"Faded","Alan Walker",1200000,"2026-05-18"),
(5,"Heat Waves","Glass Animals",980000,"2026-06-01"),
(6,"Blinding Lights","The Weeknd",1500000,"2026-04-12"),
(7,"Closer","The Chainsmokers",1100000,"2026-07-05"),
(8,"Havana","Camila Cabello",900000,"2026-08-10");

select *
from songs
order by play_count desc,added_date desc
limit 3;


