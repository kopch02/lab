select p.id_rooms, r.id_building, 
sum(to_date(p.date_departure)-to_date(p.date_entry)) "days",
sum((to_date(p.date_departure)-to_date(p.date_entry)) *p.price) "price"
from payment p, rooms r
where p.id_rooms = r.id
group by p.id_rooms, r.id_building
/