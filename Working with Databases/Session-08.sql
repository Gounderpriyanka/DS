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
select payment_method,count(*) as Payment_method
from upi
group by payment_method;

-- Task 3
select user_id,sum(amount) as Total_amount
from upi
group by user_id;