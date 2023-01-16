-- Write an SQL query to report the second highest salary from the Employee table. 
-- If there is no second highest salary, the query should report null.
-- Have to use function like MAX() or IFNULL(), otherwise the query won't return null
-- Write your MySQL query statement below

select IFNULL(
    (select distinct salary
    from Employee
    order by salary desc
    limit 1,1), null) as SecondHighestSalary;