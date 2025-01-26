select d.name Department,e.name Employee,e.salary Salary from Employee e join Department d 
on e.departmentid=d.id
where (e.salary,d.name) in (select max(salary) as max_salary,d.name as id from Employee e join Department d 
on e.departmentid=d.id
group by d.name) 
   