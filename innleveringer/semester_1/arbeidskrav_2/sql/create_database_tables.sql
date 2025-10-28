
/*
This file creates the SQL tables for the library database.
IF NOT EXISTS is used to avoid errors if tables already exist.
*/

-- Table for books
CREATE TABLE IF NOT EXISTS `books` (
    `isbn`          VARCHAR(20)      PRIMARY KEY,
    `title`         VARCHAR(255)     NOT NULL,
    `author`        VARCHAR(100)     NOT NULL,
    `publisher`     VARCHAR(100)     NOT NULL,
    -- Ensure published year is realistic (between 1000 and 9999)
    `published_year` SMALLINT UNSIGNED NOT NULL CHECK (`published_year` BETWEEN 1000 AND 9999),
    -- Ensure page count is positive (books must have at least one page)
    `page_count`    INT              NOT NULL CHECK (`page_count` > 0)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table for book copies
CREATE TABLE IF NOT EXISTS `copies` (
    `isbn`   VARCHAR(20) NOT NULL,
    `copy_number` INT     NOT NULL,
    PRIMARY KEY (`isbn`, `copy_number`),
    CONSTRAINT `fk_copies_books`
        FOREIGN KEY (`isbn`)
        REFERENCES `books` (`isbn`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table for library members
CREATE TABLE IF NOT EXISTS `members` (
    `member_id`  INT AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(50)  NOT NULL,
    `last_name`  VARCHAR(50)  NOT NULL,
    `address`    VARCHAR(255) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table for loans
CREATE TABLE IF NOT EXISTS `loans` (
    `loan_id`       INT AUTO_INCREMENT PRIMARY KEY,
    `member_id`     INT          NOT NULL,
    `isbn`          VARCHAR(20)  NOT NULL,
    `copy_number`   INT          NOT NULL,
    `loan_date`     DATE         NOT NULL,
    `returned`      TINYINT(1)   NOT NULL CHECK (`returned` IN (0, 1)),
    CONSTRAINT `fk_loans_members`
        FOREIGN KEY (`member_id`)
        REFERENCES `members` (`member_id`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT `fk_loans_copies`
        FOREIGN KEY (`isbn`, `copy_number`)
        REFERENCES `copies` (`isbn`, `copy_number`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;