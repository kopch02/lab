select c.last_mane, avg((to_date(p.date_departure)-to_date(p.date_entry)) * p.price) "avg"
from client c join payment p on c.id=p.id_client
group by c.last_mane
/
