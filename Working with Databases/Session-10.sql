-- Task 1.Create two tables: Influencers (id, name) and Collaborations (id, influencer1_id, influencer2_id, collab_date).
-- Write a SQL FULL JOIN query to list all influencers and show their collaboration partner names if any,
-- including influencers with no collaborations.
use products;

create table Influencers(
	id int primary key,
    name varchar(50)
    );
    
create table collaborations(
	id int primary key,
    influencer1_id int,
    influencer2_id int,
    foreign key (influencer1_id) references Influencers(id),
    foreign key (influencer2_id) references Influencers(id),
    collab_date date);
    
insert into Influencers values
(1,"Priya"),
(2,"Rahul"),
(3,"Neha"),
(4,"Amit"),
(5,"Sneha");

insert into collaborations value
(101,1,2,"2026-10-01");

insert into collaborations values
(102,2,3,"2026-10-03"),
(103,1,4,"2026-10-05"),
(104,3,4,"2026-10-08");

select *       
from Influencers 
left JOIN collaborations 
on Influencers.id = collaborations.influencer1_id;

-- Task 2
-- Using a SELF JOIN, write a query on a table called Playlists (id, user_id, playlist_name, parent_playlist_id) 
-- to display each playlist alongside its parent playlist name, similar to how Spotify shows nested playlists.
-- Join Playlists with itself on parent_playlist_id = id.

create table Playlists
(
	id int primary key,
    user_name varchar(50),
    playlist_name varchar(50),
    parent_playlist_id int,
    foreign key (parent_playlist_id)
    references playlists(id)
);

Insert into playlists values
(1,101,"My Music",null),
(2,101,"Workout",1),
(3,101,"Running Songs",2),
(4,102,"Chill Music",null),
(5,102,"Relaxing Songs",4),
(6,103,"Travel songs",null),
(7,103,"Road Trip",6),
(8,104,"Study Music",null);


select p.playlist_name,parent.playlist_name as parent_playlist_name
from playlists p
left join playlists parent
on p.parent_playlist_id = parent.id;

-- Task 3 
-- Given three tables: Users (id, username), Orders (id, user_id, order_date), and Payments (id, order_id, amount),
-- write a SQL query using multiple JOINs to display each username, their order date, and payment amount, showing
-- all users even if they have no orders or payments.


create table Users
(id int primary key,
username varchar(50));

insert into Users values
(1,"Priya"),
(2,"Rahul"),
(3,"Neha"),
(4,"Amit"),
(5,"Sneha");

create table Orders
(id int primary key,
user_id int,
order_date date,
foreign key(user_id)
references Users(id));

insert into Orders values
(101,1,"2026-10-01"),
(102,1,"2026-10-03"),
(103,2,"2026-10-04"),
(104,3,"2026-10-06"),
(105,5,"2026-10-08");

create table Payments
(	id int primary key,
	order_id int,
    amount int,
    foreign key(order_id)
    references Orders(id)
);

insert into  Payments values
(201,101,500),
(202,102,1200),
(203,103,750),
(204,105,2000);

select u.username,o.order_date,p.amount
from users u 
left join orders o
on u.id = o.user_id
left join payments p
on o.id = p.order_id;


-- Task 4
-- You notice that your JOIN query between Zomato's Restaurants and Reviews tables is returning duplicate
-- rows for some restaurants. Modify your query to eliminate duplicates and explain in one line 
-- why the duplicates were happening.Use DISTINCT or GROUP BY and consider the relationship between
-- restaurants and reviews.

create table restaurant
(id int primary key,
restaurant_name varchar(50)
);

insert into restaurant values
(1,"Spice Garden"),
(2,"Pizza Hub"),
(3,"Green Bowl"),
(4,"Burger Point");

create table Reveiws
(id int primary key,
restaurant_id int,
customer_name varchar(50),
rating int,
foreign key(restaurant_id)
references restaurant(id));

insert into reveiws values
(101,1,"Rahul",5),
(102,1,"Priya",4),
(103,1,"Neha",5),
(104,2,"Amit",3),
(105,2,"Sneha",4),
(106,3,"Rahul",5);









