-- A script that creates the table force_name on the MySQL server.
-- The script does not fail if force_name already exitst
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);