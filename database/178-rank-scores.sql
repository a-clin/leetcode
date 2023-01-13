-- If we could count, for each score S1.score, the number of distinct scores S2.score that are greater than or equal to this score, then this would effectively give us the ranking of S1.score

select s1.score,
    (select count(distinct s2.score)
    from scores s2
    where s2.score >= s1.score) as 'rank'
from scores s1
order by s1.score desc;


-- select score, 
--     DENSE_RANK() OVER (order by score DESC) as 'rank'
-- from Scores;