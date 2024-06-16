select c.last_mane, sum(to_date(date_departure) - to_date(date_entry))*p.price "avg"
from client c join payment p on c.id = p.id_client
group by c.last_mane, p.price
having sum(to_date(date_departure) - to_date(date_entry))*p.price > (select avg(sum) from
(
select sum(to_date(date_departure) - to_date(date_entry))*p.price as sum
from payment p join client c on p.id_client = c.id
group by c.last_mane, p.price
)
)
/