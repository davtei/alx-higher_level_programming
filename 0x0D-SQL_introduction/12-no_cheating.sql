-- A script that updates the score of Bob to 10 in the table second_table.
-- Only the name field is used (not Bob's id value)
UPDATE `second_table`
SET `score` = 10
WHERE `name` = "Bob";