-- A script that lists all records with a score >= 10 in the table second_table
-- Score and name are displayed
-- Records are ordered in descending order based on score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;