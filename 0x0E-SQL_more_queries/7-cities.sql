-- A script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on the MySQL server.
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- The script does not fail if hbtn_0d_usa and cities already exitst
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    PRIMARY KEY(id),
    id INT              UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT        NOT NULL,
    name VARCHAR(256)   NOT NULL,
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);