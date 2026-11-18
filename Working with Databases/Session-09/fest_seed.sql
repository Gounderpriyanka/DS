
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


select s.student_name,r.reg_id
from students s
left join registrations r on r.student_id = s.student_id
where r.reg_id is null;

-- Task 4.Finish 'fest_joins_part1.sql' with a RIGHT JOIN query that starts from registrations,
-- keeps every event, and returns only events nobody registered for.
-- Confirm it returns exactly 2 rows (events 7 and 8), then run the whole file top to bottom. 
-- Hint: With a RIGHT JOIN, the table written after JOIN keeps all of its rows.

select e.event_name,r.event_id
from registrations r
right  join events e on r.event_id = e.event_id
where r.reg_id is null;

