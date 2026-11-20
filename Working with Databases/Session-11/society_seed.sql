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

-- task 2.Create 'society_subqueries.sql' with a WHERE subquery that returns every meter reading
-- whose units_kwh is above the overall average, using `(SELECT AVG(units_kwh) FROM meter_readings)`.
-- Run it and save the row count as a comment. 
-- Hint: A subquery used with a comparison operator must return exactly one value, and it goes inside brackets.


SELECT *
FROM meter_readings
WHERE units_kwh > (
    SELECT AVG(units_kwh)
    FROM meter_readings
); -- 272 rows

-- 3.Add a nested query to 'society_subqueries.sql' that returns flat_id, tower and bhk for flats
-- whose yearly total bill is above the average yearly bill per flat. Use IN with a subquery that groups
-- readings by flat_id with HAVING, and inside HAVING use a second subquery for the 
-- average (`SUM(bill_inr) / COUNT(DISTINCT flat_id)` over all readings). Save the flat count as a comment.

select f.flat_id ,f.tower,f.bhk
from flats f
where flat_id in (
	select flat_id
    from meter_readings
    group by flat_id
    having sum(bill_inr) > (
		select sum(bill_inr) / count(distinct flat_id)
        from meter_readings) 
); -- 23

-- task 4.Finish 'society_subqueries.sql' with a subquery in the SELECT list that shows flat_id, tower
-- and each flat's total units for the year as total_units, then run the whole file.
-- Check that the 50 total_units values add up to `SELECT SUM(units_kwh) FROM meter_readings`,
-- and save both numbers as comments. Hint: The inner query refers to the outer row, 
-- like `WHERE m.flat_id = f.flat_id`.

select f.flat_id,f.tower,sum(units_kwh) as total_units
from flats f
join meter_readings m on f.flat_id = m.flat_id
group by flat_id; 

-- Q4: Display yearly total units for every flat
SELECT
    f.flat_id,
    f.tower,
    (
        SELECT SUM(m.units_kwh)
        FROM meter_readings m
        WHERE m.flat_id = f.flat_id
    ) AS total_units
FROM flats f;

-- Sum of the 50 total_units values
SELECT SUM(total_units)
FROM (
    SELECT
        f.flat_id,
        (
            SELECT SUM(m.units_kwh)
            FROM meter_readings m
            WHERE m.flat_id = f.flat_id
        ) AS total_units
    FROM flats f
) AS yearly_totals; -- 165448

-- Sum of all meter readings
SELECT SUM(units_kwh)
FROM meter_readings; -- 165448
