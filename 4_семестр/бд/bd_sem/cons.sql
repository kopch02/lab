select t1.table_name, t1.constraint_name,
t2.column_name, t1.constraint_type
from user_constraints t1, user_cons_columns t2
where t1.constraint_name = t2.constraint_name
and lower(t1.table_name) = '&1'
/