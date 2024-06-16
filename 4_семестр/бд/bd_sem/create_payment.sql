create table payment
(
    id NUMBER(7) constraint payment_id_pk  PRIMARY KEY,
    price NUMBER(7) constraint payment_price_nn NOT NULL,
    date_entry VARCHAR2(20) constraint payment_de_nn NOT NULL,
    date_departure VARCHAR2(20) constraint payment_dd_nn NOT NULL,
    id_rooms NUMBER(7) constraint payment_idrooms_fk REFERENCES rooms(id),
    id_client NUMBER(7) constraint payment_idclient_fk REFERENCES client(id)
)
/