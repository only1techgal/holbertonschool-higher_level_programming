-- This script lists all the tables of a database
SELECT table_name
FROM INFORMATION_SCHEMA.TABLES
WHERE table_type = 'BASE TABLE'
