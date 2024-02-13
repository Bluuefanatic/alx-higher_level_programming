-- list_records_with_names.sql
-- This script lists all records of the table second_table in the specified database with a name value, ordered by descending score


-- List records with a name value, displaying both score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
