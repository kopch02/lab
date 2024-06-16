create table building
(
id NUMBER(7) constraint build_id_pk PRIMARY KEY,
floors NUMBER(3) constraint build_floors_nn NOT NULL,
class VARCHAR2(20) constraint build_class_nn NOT NULL,
numbers_rooms NUMBER(4) constraint build_numrooms_nn NOT NULL
)
/