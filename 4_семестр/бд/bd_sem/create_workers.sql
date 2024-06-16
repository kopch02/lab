create table workers
(
    id  NUMBER(7) constraint workers_id_pk PRIMARY KEY,
    post VARCHAR2(30) constraint workers_post_nn NOT NULL,
    first_name VARCHAR2(20) constraint workers_fn_nn NOT NULL,
    last_mane VARCHAR2(20) constraint workers_Ln_nn NOT NULL,
    salary NUMBER(7) constraint workers_salary_nn NOT NULL,
    id_building NUMBER(7) constraint workers_id_bild_fk REFERENCES building(id)
)
/
