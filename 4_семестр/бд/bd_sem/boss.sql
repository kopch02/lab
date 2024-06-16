column column_name format a15
column table_name format a15
column constraint_name format a15
@@drop building
@@drop workers
@@drop servis
@@drop client
@@drop rooms
@@drop payment
@@create_building
@@create_workers
@@create_servis
@@create_client
@@create_rooms
@@create_payment
desc workers
desc building
desc servis
desc client
desc rooms
desc payment
@@insert_building 1 80 5 700
@@insert_workers 1 president Ivan Sidorov 100000 1
@@insert_servis 1 plus plus
@@insert_client 1 Alexsandr Ivanov 1234567890 89005553535
@@insert_rooms 1 1 taken 2 1 
@@insert_payment 1 12000 01-06-22 08-06-22 1 1

@@insert_payment 4 12000 02-06-22 04-06-22 1 1

@@insert_building 2 100 4 1300
@@insert_workers 2 concierge Petr Kuznetcov 30000 1
@@insert_servis 2 minus plus
@@insert_client 2 Anton Sergeev 4334567890 89005643535
@@insert_rooms 2 1 taken 1 2 
@@insert_payment 2 5000 01-05-22 25-06-22 2 2

@@insert_building 3 60 4 500
@@insert_workers 3 cleaner Maxim Inurov 15000 2
@@insert_servis 3 minus minus
@@insert_client 3 Dmitryi Sobolev 1237657890 89995553535
@@insert_rooms 3 2 taken 2 1 
@@insert_payment 3 12000 16-05-22 20-05-22 3 3

@@cons workers
@@cons building
@@cons servis
@@cons client
@@cons payment
@@cons rooms
SELECT * FROM workers;
SELECT * FROM building;
SELECT * FROM servis;
SELECT * FROM client;
SELECT * FROM payment;
SELECT * FROM rooms;

@@skript1
@@skript2
@@skript3
@@skript4





