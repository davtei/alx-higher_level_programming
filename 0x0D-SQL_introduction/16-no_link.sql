-- A script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Rows without a name value are not listed
-- Score and name are displayed in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC