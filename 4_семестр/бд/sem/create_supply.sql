create table supply
(
id NUMBER(7) constraint suppl_id_pk PRIMARY KEY,
part_id NUMBER(9) constraint suppl_part_id_fk REFERENCES parts(id),
supler_id NUMBER(7) constraint suppl_suppler_id_fk REFERENCES suppliers(id),
date_ Date constraint supply_date_nn NOT NULL,
price VARCHAR2(10) constraint supply_price_nn NOT NULL,
quantity VARCHAR2(10) constraint supply_quan_nn NOT NULL
)
/