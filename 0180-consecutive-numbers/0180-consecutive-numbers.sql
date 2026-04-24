select DISTINCT(f.num) as ConsecutiveNums from Logs f join Logs s on f.id+1=s.id join Logs t on f.id+2=t.id
where f.num=s.num and f.num=t.num 