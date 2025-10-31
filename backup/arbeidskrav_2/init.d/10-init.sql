CREATE DATABASE IF NOT EXISTS ga_bibliotek;
CREATE USER IF NOT EXISTS 'app_user'@'%' IDENTIFIED BY 'secure_app_password';
GRANT ALL PRIVILEGES ON ga_bibliotek.* TO 'app_user'@'%';
FLUSH PRIVILEGES;