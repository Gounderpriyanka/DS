-- Task 2
create database foodie_app;

-- Task 3
use foodie_app;

create table restaurants(
	id int primary key,
    name varchar(100),
    cuisine varchar(50),
    rating decimal,
    location varchar(100)
);

-- Task 4
create table users(
	user_id int primary key,
    username varchar(100),
    email varchar(50),
    phone_number int,
    created_at datetime 
)


