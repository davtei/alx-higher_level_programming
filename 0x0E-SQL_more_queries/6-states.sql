-- A script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on the MySQL server.
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- The script does not fail if hbtn_0d_usa and states already exitst
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    PRIMARY KEY(id),
    id INT              UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256)   NOT NULL
);