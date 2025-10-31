
/*
This file creates the database.
IF NOT EXISTS is used to avoid errors if tables already exist.
*/

-- Checking if database exists and drops it
DROP DATABASE IF EXISTS ga_bibliotek;

-- Creating the database
CREATE DATABASE ga_bibliotek
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Instructing the usage of the database
USE ga_bibliotek;