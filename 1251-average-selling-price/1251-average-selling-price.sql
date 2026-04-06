select p.product_id,
    ROUND(
        COALESCE(SUM(u.units * p.price) / SUM(u.units), 0), 
        2
    ) AS average_price
from prices p
left join UnitsSold u
ON p.product_id=u.product_id AND 
purchase_date BETWEEN start_date And end_date
group by p.product_id