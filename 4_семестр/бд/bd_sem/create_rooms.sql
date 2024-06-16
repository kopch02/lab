create table rooms
(
id NUMBER(7) constraint rooms_id_nn_uq NOT NULL UNIQUE,
id_building NUMBER(7) constraint rooms_id_bild_fk REFERENCES building(id),
condition VARCHAR2(20) constraint rooms_condition_nn NOT NULL,
capacity NUMBER(2) constraint rooms_capacity_nn NOT NULL,
id_servis NUMBER(2) constraint rooms_idservis_fk REFERENCES servis(id)
)
/

