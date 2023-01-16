select department, employee, salary
from (select e.name as Employee, 
        d.name as Department,
        e.salary,
        dense_rank() over(PARTITION by e.departmentId order by salary desc) as rk
FROM Employee e join Department d on e.departmentId = d.id ) T
where rk <= 3;
