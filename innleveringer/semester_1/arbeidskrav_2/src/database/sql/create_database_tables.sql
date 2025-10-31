
/*
This file creates the SQL tables for the library database.
IF NOT EXISTS is used to avoid errors if tables already exist.
*/

-- Table for books
CREATE TABLE IF NOT EXISTS `bok` (
    `ISBN`              VARCHAR(20)      PRIMARY KEY,
    `Tittel`            VARCHAR(255)     NOT NULL,
    `Forfatter`         VARCHAR(100)     NOT NULL,
    `Forlag`            VARCHAR(100)     NOT NULL,
    -- Ensure published year is realistic (between 1000 and 9999)
    `UtgittÅr`          SMALLINT UNSIGNED NOT NULL CHECK (`UtgittÅr` BETWEEN 1000 AND 9999),
    -- Ensure page count is positive (books must have at least one page)
    `AntallSider`       INT              NOT NULL CHECK (`AntallSider` > 0)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table for book copies
CREATE TABLE IF NOT EXISTS `eksemplar` (
    `ISBN`          VARCHAR(20) NOT NULL,
    `EksNr`         INT     NOT NULL,
    PRIMARY KEY (`ISBN`, `EksNr`),
    CONSTRAINT `fk_copies_books`
        FOREIGN KEY (`ISBN`)
        REFERENCES `bok` (`ISBN`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table for library members
CREATE TABLE IF NOT EXISTS `låner` (
    `LNr`               INT AUTO_INCREMENT PRIMARY KEY,
    `Fornavn`           VARCHAR(50)  NOT NULL,
    `Etternavn`         VARCHAR(50)  NOT NULL,
    `Addresse`          VARCHAR(255) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table for loans
CREATE TABLE IF NOT EXISTS `utlån` (
    `UtlånsNr`          INT AUTO_INCREMENT PRIMARY KEY,
    `LNr`               INT          NOT NULL,
    `ISBN`              VARCHAR(20)  NOT NULL,
    `EksNr`             INT          NOT NULL,
    `Utlånsdato`        DATE         NOT NULL,
    `Levert`            TINYINT(1)   NOT NULL CHECK (`Levert` IN (0, 1)),
    CONSTRAINT `fk_loans_members`
        FOREIGN KEY (`LNr`)
        REFERENCES `låner` (`LNr`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT `fk_loans_copies`
        FOREIGN KEY (`ISBN`, `EksNr`)
        REFERENCES `eksemplar` (`ISBN`, `EksNr`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;