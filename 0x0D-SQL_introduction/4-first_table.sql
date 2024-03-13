-- Write a script that creates a table called first_table in the current database in your MySQL server.
create table if not EXISTS first_table(
	id int,
	name varchar(256)
)
