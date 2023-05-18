-- A script that creates the table unique_id on the MySQL server.
-- id INT with the default value 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256))