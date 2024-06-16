@@drop auto
@@drop customer
@@drop orders
@@drop parts
@@drop suppliers
@@drop supply
@@drop auto_type
@@create_auto
@@create_type
@@create_suppliers
@@create_customer
@@create_part
@@create_order
@@create_supply
desc auto
desc customer
desc orders
desc suppliers
desc parts
desc supply
desc auto_type
@@insert_auto 1 Toyota Camry 2012
@@insert_type 1 1 CamryEngine
@@insert_suppliers 1 DetailsFast Moscow
@@insert_parts 1 engine 10000 2 1
@@insert_supply 1 1 1 22-10-2015 30000 3
@@insert_customer 1 FirstCustomer 88005553535
@@insert_order 1 24-10-2015 12000 1 1
@@insert_auto 2 Toyota Corolla 2013
@@insert_type 2 2 CorollaEngine
@@insert_parts 2 engine 9000 1 2
@@insert_supply 2 2 1 23-10-2015 9000 1
@@insert_customer 2 SecondCustomer 88005553536
@@insert_order 2 25-10-2015 10000 2 2
SELECT * FROM auto;
SELECT * FROM auto_type;
SELECT * FROM suppliers;
SELECT * FROM parts;
SELECT * FROM supply;
SELECT * FROM customer;
SELECT * FROM orders;
