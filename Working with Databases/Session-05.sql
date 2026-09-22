-- Task 1

use foodie_app;
select * from restaurants;

alter table restaurants
rename column location to  city;

insert into restaurants value
(1,"Swagat Restaurant","South Indian","4.3","Ahmedabad");

alter table restaurants
modify column rating decimal(2,1);

update restaurants
set rating = 4.3
where id = 1;

insert into restaurants values
(2,"Swadisht Bhojanalay","Gujarati",4.1,"Surat"),
(3,"Spice Hub","Chinese",4.5,"Ahmedabad"),
(4,"Pizza Palace","Italian",3.8,"Surat"),
(5,"Royal Tandoor","North Indian",4.6,"Ahmedabad"),
(6,"Swaad Corner","South Indian",3.6,"Surat"),
(7,"Dragon House","Chinese",4.2,"Ahmedabad"),
(8,"Pasta Point","Italian",3.4,"Surat"),
(9,"Urban Bites","Fast Food",4.0,"Ahmedabad"),
(10,"Swara Cafe","Italian",3.9,"Vadodara");

-- Task 2
select name, cuisine,rating,city
from restaurants
where city in ("Ahmedabad","surat") and rating>4.0;

-- Task 3 
Select name , city
from restaurants
where name like "swa%";

-- Task 4
select name, city,rating
from restaurants
where rating between 3.5 and 4.5;

-- Task 5
select name,cuisine
from restaurants
where cuisine in ("Chinese","Italian","South Indian")


