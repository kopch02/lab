create table parts
(
id NUMBER(9) constraint part_id_pk PRIMARY KEY,
part_name VARCHAR2(100),
price VARCHAR2(8) constraint parts_price_nn NOT NULL,
quantity VARCHAR2(8) constraint parts_quan_nn NOT NULL,
parts_type_id NUMBER(7) constraint parts_type_id_fk REFERENCES auto_type(id)
)
/