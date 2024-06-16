create table auto
(
id NUMBER(7) constraint auto_id_pk PRIMARY KEY,
brand VARCHAR2(50) constraint auto_brand_nn NOT NULL,
model VARCHAR2(50) constraint auto_model_nn NOT NULL,
year_ CHAR(4) constraint auto_year_nn NOT NULL
)
/