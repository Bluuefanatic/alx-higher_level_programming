-- list_high_score_records.sql
-- This script lists records with a score >= 10 in the table second_table in the specified database, ordered by score

-- Select records with score >= 10, displaying both score and name, ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
