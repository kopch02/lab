create table orders
(
id NUMBER(7) constraint ord_id_pk PRIMARY KEY,
ord_date Date constraint ord_date_nn NOT NULL,
price VARCHAR2(10) constraint ord_price_nn NOT NULL,
part_id NUMBER(9) constraint ord_part_id_fk REFERENCES parts(id),
cust_id NUMBER(7) constraint ord_cust_id_fk REFERENCES customer(id)
)
/