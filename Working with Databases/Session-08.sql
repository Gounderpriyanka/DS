-- Task 1
use products;

create table upi(
	order_id int primary key,
    user_id int,
    payment_method varchar(100),
    amount int
);

insert into upi values
(1,101,"UPI",450),
(2,102,"Card",250),
(3,101,"Wallet",350),
(4,103,"UPI",600),
(5,102,"COD",200),
(6,104,"Card",500),
(7,101,"UPI",300),
(8,103,"Wallet",400),
(9,104,"UPI",700),
(10,102,"Card",550);

-- Task 2
select payment_method,count(*) as orders_count
from upi
group by payment_method;

-- Task 3
select user_id,sum(amount) as Total_amount
from upi
group by user_id;

-- Task 4
select payment_method , avg(amount)
from upi
group by payment_method
having avg(amount)>300;

-- Task 5
-- where example
select payment_method , count(*) as no_of_orders
from upi
where amount > 300
group by payment_method;

-- Having example 
select payment_method , avg(amount)
from upi
group by payment_method
having avg(amount)>300;



