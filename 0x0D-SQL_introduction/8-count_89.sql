-- count_records.sql
-- This script displays the number of records with id = 89 in the table first_table in the specified database

-- Count the number of records with id = 89
SELECT COUNT(*) AS record_count FROM first_table WHERE id = 89;
