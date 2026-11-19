use fest_db;
select * from events;
select * from registrations;
select * from students;

-- 1.Create 'fest_joins_part2.sql' with a SELF JOIN that joins students to itself on referred_by,
--  returning student_name as student and the referrer's name as referred_by_name for every referred student.
-- Run it and confirm the row count equals the number of non-NULL referred_by values. 
-- Hint: Use two aliases of the same table, `s` and `ref`. 
-- If you missed Session 9, build a students table with 20 rows and a referred_by column first.

select s.student_name as student,ref.student_name as referred_by_name
from students s
join students ref on s.referred_by = ref.student_id;

-- Task 2.Add a multiple-join query to 'fest_joins_part2.sql' that joins registrations, students, 
-- events and a second copy of students for the referrer, returning reg_id, student_name, event_name,
-- fee_inr and referred_by_name for all registrations. Students without a referrer must still appear.
-- Confirm exactly 200 rows. Hint: Use LEFT JOIN for the referrer copy.

select r.reg_id,s.student_name,e.event_name,e.fee_inr,ref.student_name as referred_by_name
from registrations r
join students s on r.student_id = s.student_id
join events e on r.event_id = e.event_id
left join students ref  ON s.referred_by = ref.student_id ;


-- Task 3.Insert five duplicate registrations (reg_id 201 to 205) that repeat five existing student_id 
-- and event_id pairs, then add a query that finds those pairs, showing student_name, 
-- event_name and the number of times registered. Confirm exactly 5 rows, each with count 2.
-- Hint: Group by student_id, event_id, student_name and event_name, then filter with `HAVING COUNT(*) > 1`.


insert into registrations values
(201,25,3,"2026-10-13"),
(202,13,6,"2026-10-05"),
(203,33,4,"2026-10-22"),
(204,36,3,"2026-10-21"),
(205,36,6,"2026-10-10");

select s.student_name,e.event_name , count(*)
from registrations r
join students s on r.student_id = s.student_id
join events e on r.event_id = e.event_id
group by r.student_id,r.event_id,e.event_name,s.student_name
having count(*) > 1;


-- Task 4.Finish 'fest_joins_part2.sql' with a full join of students and registrations that runs on both 
-- MySQL and PostgreSQL: a LEFT JOIN and a RIGHT JOIN combined with UNION, selecting student_id, student_name,
-- reg_id and event_id. Confirm 215 rows (205 registrations plus 10 students with none),
-- use ON for every join, list columns instead of `*`, and run the whole file.

select r.student_id,s.student_name,r.reg_id,r.event_id
from students s 
left join registrations r on s.student_id = r.student_id
union 
select r.student_id,s.student_name,r.reg_id,r.event_id
from students s 
right join registrations r on s.student_id = r.student_id;















