# Write your MySQL query statement below
select 
   ss.student_id,ss.student_name,ss.subject_name,count(e.subject_name) as attended_exams
from 
(select 
    student_id,s.student_name,sub.subject_name
from 
    Students s
cross join 
    Subjects sub) ss
left join 
        Examinations e
on 
    ss.student_id=e.student_id
AND
   ss.subject_name=e.subject_name 
group by
    ss.student_id,
    ss.student_name,
    ss.subject_name
order by
    ss.student_id asc,
    ss.student_name asc;    





   

