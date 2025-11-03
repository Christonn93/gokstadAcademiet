/*
This file creates the SQL tables for the library database.
IF NOT EXISTS is used to avoid errors if tables already exist.
*/

-- Table: bok
CREATE TABLE IF NOT EXISTS `bok` (
    `ISBN`          VARCHAR(20)      PRIMARY KEY,
    `Tittel`        VARCHAR(255)     NOT NULL,
    `Forfatter`     VARCHAR(100)     NOT NULL,
    `Forlag`        VARCHAR(100)     NOT NULL,
    `UtgittÅr`      SMALLINT UNSIGNED NOT NULL CHECK (`UtgittÅr` BETWEEN 1000 AND 9999),
    `AntallSider`   INT              NOT NULL CHECK (`AntallSider` > 0)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table: eksemplar
CREATE TABLE IF NOT EXISTS `eksemplar` (
    `ISBN`      VARCHAR(20) NOT NULL,
    `EksNr`     INT NOT NULL,
    PRIMARY KEY (`ISBN`, `EksNr`),
    CONSTRAINT `fk_eksemplar_bok`
        FOREIGN KEY (`ISBN`)
        REFERENCES `bok` (`ISBN`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table: låner
CREATE TABLE IF NOT EXISTS `låner` (
    `LNr`       INT AUTO_INCREMENT PRIMARY KEY,
    `Fornavn`   VARCHAR(50)  NOT NULL,
    `Etternavn` VARCHAR(50)  NOT NULL,
    `Adresse`   VARCHAR(255) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table: utlån
CREATE TABLE IF NOT EXISTS `utlån` (
    `UtlånsNr`   INT AUTO_INCREMENT PRIMARY KEY,
    `LNr`        INT          NOT NULL,
    `ISBN`       VARCHAR(20)  NOT NULL,
    `EksNr`      INT          NOT NULL,
    `Utlånsdato` DATE         NOT NULL,
    `Levert`     TINYINT(1)   NOT NULL CHECK (`Levert` IN (0, 1)),
    CONSTRAINT `fk_utlån_låner`
        FOREIGN KEY (`LNr`)
        REFERENCES `låner` (`LNr`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT `fk_utlån_eksemplar`
        FOREIGN KEY (`ISBN`, `EksNr`)
        REFERENCES `eksemplar` (`ISBN`, `EksNr`)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
