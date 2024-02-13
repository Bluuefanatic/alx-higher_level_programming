-- print_table_description.sql
-- This script prints the full description of the table first_table in the specified database

-- Extract table information from information_schema
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = '$1' AND TABLE_NAME = 'first_table';
