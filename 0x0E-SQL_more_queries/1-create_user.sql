-- A script that creates the MySQL server user user_0d_1
-- user_0d_1 has all privileges on the MySQL server
-- user_0d_1 password is set to user_0d_1_pwd
-- The script does not fail if user_0d_1 already exitst
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT *.* TO user_0d_1@localhost