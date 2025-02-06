# Write your MySQL query statement below
select product_name,sum(unit) unit from Products
join Orders
using(product_id)
where month(order_date)=2 and year(order_date)=2020
group by product_id
having unit>=100