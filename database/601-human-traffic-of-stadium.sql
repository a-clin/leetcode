# Write your MySQL query statement below
with t as (select *,
    id - row_number() over(order by id) as grp
    from stadium 
    where people >= 100)

select t.id, t.visit_date, t.people
from t
where grp in (select grp from t 
group by grp;
having count(*) >= 3)

