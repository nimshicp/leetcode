# Write your MySQL query statement below
select r.contest_id,ROUND((COUNT(r.user_id)/ (SELECT COUNT(*) FROM Users))*100,2)AS percentage from Users u
right join Register r 
on u.user_id=r.user_id
group by r.contest_id  order by percentage DESC , contest_id ASC
