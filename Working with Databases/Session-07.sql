-- Task 1
use products;

create table Orders(
	order_id int primary key,
    user_name varchar(100),
    Total_amount int,
    order_date date
);

Select * from Orders;

insert into Orders value(1,"Sam",2500,"2026-09-20");

insert into Orders values
(2,"Rahul",1800,"2026-09-20"),
(3,"Sam",3200,"2026-09-21"),
(4,"Neha",NULL,"2026-09-22"),
(5,"Rahul",4500,"2026-09-23");

-- Task 2
select user_name, count(*) as order_count
from Orders
group by user_name;

-- Task 3
select avg(total_amount) as total
from orders;

-- Task 4
select min(total_amount) as min_amount,max(total_amount) as max_amount
from orders;

-- task 5
select sum(total_amount) as total_sales
from orders
where total_amount is not null;