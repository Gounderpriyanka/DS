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
where id = 1
