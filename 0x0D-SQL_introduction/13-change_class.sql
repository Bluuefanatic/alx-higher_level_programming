-- remove_low_score_records.sql
-- This script removes all records with a score <= 5 in the table second_table in the specified database

-- Remove records with a score <= 5
DELETE FROM second_table WHERE score <= 5;
