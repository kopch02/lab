create table auto_type
(
id NUMBER(7) constraint type_id_pk PRIMARY KEY,
auto_id constraint type_auto_id_fk REFERENCES auto(id),
comments VARCHAR2(100)
)
/