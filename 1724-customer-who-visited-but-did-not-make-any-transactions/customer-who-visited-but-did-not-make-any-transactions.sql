# Write your MySQL query statement below
select v.customer_id,count(*) as 'count_no_trans'
from visits v 
where v.visit_id not in (select t.visit_id from transactions t)
group by customer_id;