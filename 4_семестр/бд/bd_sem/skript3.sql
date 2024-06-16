select avg(sum((to_date(date_departure) - to_date(date_entry))*p.price))
from payment p join client c on p.id_client = c.id
group by c.last_mane
/