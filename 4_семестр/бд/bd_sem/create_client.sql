create table client
(
id NUMBER(7) constraint client_id_pk PRIMARY KEY,
first_name VARCHAR2(20) constraint client_fn_nn NOT NULL,
last_mane VARCHAR2(20) constraint client_Ln_nn NOT NULL,
passport_data VARCHAR2(10) constraint client_passport_nn_uq NOT NULL UNIQUE,
phone_number VARCHAR2(11) constraint client_phone_nn_uq NOT NULL UNIQUE
)
/