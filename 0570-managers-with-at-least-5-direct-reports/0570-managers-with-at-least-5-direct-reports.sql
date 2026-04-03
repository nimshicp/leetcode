# Write your MySQL query statement below
select name from Employee WHERE id IN(
    select managerId from Employee group by managerId HAVING COUNT(*)>=5
) 