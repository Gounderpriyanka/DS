
use fest_db;

select * from events;
select * from registrations;
select * from students;


-- Task 2.Write an INNER JOIN query in 'fest_joins_part1.sql' that lists reg_id, student_name, event_name, 
-- fee_inr and reg_date by joining registrations to students and events on their key columns.
--  Run it and confirm it returns exactly 200 rows.
-- Hint: Give the tables short aliases (`r`, `s`, `e`) and write conditions such as 
-- `ON r.student_id = s.student_id`.



select r.reg_id,s.student_name,e.event_name,e.fee_inr,r.reg_date
from registrations r
inner join students s on r.student_id = s.student_id
inner join events e on r.event_id = e.event_id;


-- Task 3.Add a LEFT JOIN query to 'fest_joins_part1.sql' that starts from students, joins registrations,
-- and keeps only students with no registration (`reg_id IS NULL`).
-- Confirm it returns exactly 10 rows, students 51 to 60. 
-- Constraint: Do not use a subquery; subqueries are taught later.


