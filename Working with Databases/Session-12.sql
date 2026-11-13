

-- 1.Create 'society_cte.sql' with a CTE named `flat_totals` (flat_id, total_units and total_bill per flat) 
-- and a final SELECT that returns flats whose total_bill is above the average total_bill across flat_totals.
-- Confirm the flat count matches your nested query from Session 11. Hint: `WITH flat_totals AS (...) 
-- SELECT ... WHERE total_bill > (SELECT AVG(total_bill) FROM flat_totals)`.
 
CREATE DATABASE society_db;
USE society_db;

-- Create flats table
CREATE TABLE flats (
    flat_id VARCHAR(10) PRIMARY KEY,
    tower VARCHAR(10),
    flat_number INT
);

-- Insert 20 flats across 4 towers
INSERT INTO flats VALUES
('A101','A',101),
('A102','A',102),
('A103','A',103),
('A104','A',104),
('A105','A',105),
('B101','B',101),
('B102','B',102),
('B103','B',103),
('B104','B',104),
('B105','B',105),
('C101','C',101),
('C102','C',102),
('C103','C',103),
('C104','C',104),
('C105','C',105),
('D101','D',101),
('D102','D',102),
('D103','D',103),
('D104','D',104),
('D105','D',105);

-- Create meter_readings table
CREATE TABLE meter_readings (
    reading_id INT AUTO_INCREMENT PRIMARY KEY,
    flat_id VARCHAR(10),
    reading_month DATE,
    total_units DECIMAL(10,2),
    total_bill DECIMAL(10,2),
    FOREIGN KEY (flat_id) REFERENCES flats(flat_id)
);

-- Insert sample readings
INSERT INTO meter_readings
(flat_id, reading_month, total_units, total_bill)
VALUES
('A101','2026-01-01',120,600),
('A102','2026-01-01',150,750),
('A103','2026-01-01',100,500),
('A104','2026-01-01',180,900),
('A105','2026-01-01',200,1000),

('B101','2026-01-01',130,650),
('B102','2026-01-01',160,800),
('B103','2026-01-01',110,550),
('B104','2026-01-01',190,950),
('B105','2026-01-01',210,1050),

('C101','2026-01-01',140,700),
('C102','2026-01-01',170,850),
('C103','2026-01-01',115,575),
('C104','2026-01-01',195,975),
('C105','2026-01-01',220,1100),

('D101','2026-01-01',125,625),
('D102','2026-01-01',155,775),
('D103','2026-01-01',105,525),
('D104','2026-01-01',185,925),
('D105','2026-01-01',230,1150);


with flat_total as (

select flat_id,
sum(total_units)  as total_units,
sum(total_bill) as total_bill
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


with tower_totals as (
	select	f.tower,
		sum(m.total_units) as tower_units
        from flats f
        join meter_readings m
        on f.flat_id = m.flat_id
        group by f.tower
),
grand_total AS (
    SELECT SUM(tower_units) AS total_units
    FROM tower_totals
)
SELECT
    tower,
    tower_units,
    ROUND(tower_units * 100.0 / total_units, 1) AS share_pct
FROM tower_totals
CROSS JOIN grand_total;




    
                                                                                                                      '''

