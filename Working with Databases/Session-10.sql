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
