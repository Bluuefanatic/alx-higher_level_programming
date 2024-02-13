-- list_second_table_records.sql
-- This script lists all records of the table second_table in the specified database, ordered by score


-- Select all records from second_table, displaying both score and name, ordered by score
SELECT score, name FROM second_table ORDER BY score DESC;
