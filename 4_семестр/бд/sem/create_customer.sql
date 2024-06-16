create table customer
(
id NUMBER(7) constraint cus_id_pk PRIMARY KEY,
full_name VARCHAR2(80) constraint cust_name_nn NOT NULL,
phone VARCHAR2(11) constraint cust_phone_nn_uq NOT NULL UNIQUE
)
/