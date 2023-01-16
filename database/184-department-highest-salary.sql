select d.name as Department,
        e.name as Employee,
        e.salary
from Employee e join Department d on e.departmentId = d.id
where (salary, departmentId) in (
    select max(salary), d2.id
    from Employee e2 join Department d2 on e2.departmentId = d2.id
    group by d2.id)