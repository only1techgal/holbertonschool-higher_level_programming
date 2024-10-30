-- This script creates a table 'second_table' in the database 'hbtn_0c_0'
CREATE TABLE IF NOT EXISTS second_table (
	id INT PRIMARY KEY,
	name VARCHAR(256),
	score INT
);

-- Deletes all records from the table
-- DELETES FROM second_table;

-- Inserts multiple rows into the second_table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8),
ON DUPLICATE KEY UPDATE 
    name = VALUES(name), 
    score = VALUES(score); 

