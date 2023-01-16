# Write your MySQL query statement below
select name as customers
from Customers c left join Orders on (c.id = customerId)
where customerId is null;