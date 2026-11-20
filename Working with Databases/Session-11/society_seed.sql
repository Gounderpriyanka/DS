use society_db ;

create table Flats(
	flat_id int primary key,
    tower varchar(50),
    bhk int
);

create table meter_readings(
	reading_id int primary key,
    flat_id int,
    reading_month date,
    units_kwh int,
    bill_inr decimal(10,2),
    foreign key (flat_id) references flats(flat_id)
);

select * from flats;
select * from meter_readings;