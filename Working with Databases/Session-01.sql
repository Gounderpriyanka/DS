create database music_streaming_app;

use music_streaming_app;

create table playlists(
	playlist_id int primary key	,
    name varchar(30),
    created_by varchar(30)

);

insert into playlists values
(1,"Bollywood Hits","Amit"),
(2,"Chill Vibes","Priya"),
(3,"Workout Mix","Rahul");

select * from playlists

/*

For a food delivery app like Zomato:
- A table is like a category of related information. For example,
 an orders table stores all food orders placed by customers.
- A row is one complete record in that table. 
For example, one row could represent Amit’s order for a pizza from Domino’s.
- A column is a specific type of information stored for every order. 
Examples include order_id, customer_name, restaurant_name, food_item, and price.

*/

