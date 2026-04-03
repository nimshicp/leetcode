# Write your MySQL query statement below
select * from Cinema where description != "boring" and id IN (
    select id from Cinema where id % 2=1 ) order by rating DESC;