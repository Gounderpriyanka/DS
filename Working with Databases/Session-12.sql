

-- 1.Create 'society_cte.sql' with a CTE named `flat_totals` (flat_id, total_units and total_bill per flat) 
-- and a final SELECT that returns flats whose total_bill is above the average total_bill across flat_totals.
-- Confirm the flat count matches your nested query from Session 11. Hint: `WITH flat_totals AS (...) 
-- SELECT ... WHERE total_bill > (SELECT AVG(total_bill) FROM flat_totals)`.
 
 use cte;
CREATE TABLE meter_readings (
    flat_id VARCHAR(10) primary key,
    units INT,
    bill DECIMAL(10,2)
);

INSERT INTO meter_readings
(flat_id,units, bill)
VALUES
('A101',  10, 1200),
('A102',  15, 1800),
('A103',  20, 2500),
('B101',  12, 1500),
('B102',  18, 2100),
('B103',  27, 3200),
('C101',  8, 1000),
('C102',  16, 1900),
('C103',  30, 3500),
('D101',  14, 1700),
('D102',  22, 2600),
('D103',  32, 3800);

with flat_total as (

select flat_id,
count(units)  as total_units,
sum(bill) as total_bill
from meter_readings
group by flat_id)

select * 
from flat_total
where total_bill>
(select avg(total_bill)
from flat_total
);



-- task 2 Add a query with two CTEs, `tower_totals` (units per tower) and `grand_total` (units overall), 
-- that returns tower, tower_units and share_pct rounded to 1 decimal. Expect 4 rows whose share_pct values 
-- add up to about 100. Hint: Separate the CTEs with a comma, and use `CROSS JOIN grand_total` to place
-- the one-row total beside each tower.


 

    
                                                                                                                      '''

