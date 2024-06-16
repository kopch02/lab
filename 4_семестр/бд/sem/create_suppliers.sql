create table suppliers
(
id NUMBER(7) constraint supls_id_pk PRIMARY KEY,
s_name VARCHAR2(100) constraint supls_name_nn_uq NOT NULL UNIQUE,
adress VARCHAR2(100) constraint supls_adr_nn_uq NOT NULL UNIQUE
)
/