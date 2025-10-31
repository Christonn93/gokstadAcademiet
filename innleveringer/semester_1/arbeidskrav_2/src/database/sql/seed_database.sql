/*
This file inserts example data into the library database tables.
Follows the structure of:
- bok
- eksemplar
- låner
- utlån
*/

-- -------------------------------
-- Insert example books
-- -------------------------------
INSERT INTO `bok` (`isbn`, `tittel`, `forfatter`, `forlag`, `utgittår`, `antallsider`) VALUES
('8203188843','Kristin Lavransdatter: Kransen','Undset, Sigrid','Aschehoug',1920,323),
('8203190483','Fyret: en ny sak for Dalgliesh','James, P. D.','Aschehoug',2005,413),
('8203191543','Lasso rundt fru Luna','Mykle, Agnar','Gyldendal',1954,614),
('8203191201','Victoria','Hamsun, Knut','Gyldendal',1898,111),
('8253029533','Jonas','Bjørneboe, Jens','Pax',1955,302),
('8274822231','Den gamle mannen og havet','Hemingway, Ernest','Gyldendal',1952,99);

-- -------------------------------
-- Insert copies of books (eksemplar)
-- -------------------------------
INSERT INTO `eksemplar` (`isbn`, `eksnr`) VALUES
('8203188843',1), ('8203188843',2),
('8203190483',1),
('8203191543',1), ('8203191543',2),
('8203191201',1),
('8253029533',1),
('8274822231',1);

-- -------------------------------
-- Insert library members (låner)
-- member_id is auto-incremented
-- -------------------------------
INSERT INTO `låner` (`fornavn`, `etternavn`, `adresse`) VALUES
('Lise','Jensen','Erling Skjalgssons gate 56'),
('Joakim','Gjertsen','Grinda 2'),
('Katrine','Garvik','Ottar Birtings gate 9'),
('Emilie','Marcussen','Kyrre Grepps gate 29'),
('Valter','Ellefsen','Fyrstikkbakken 5D'),
('Tormod','Vaaler','Lassons gate 32'),
('Asle','Eekhoff','Kirkeveien 5'),
('Birte','Aass','Henrik Wergelands Allé 47');

-- -------------------------------
-- Insert loans (utlån)
-- loan_id is auto-incremented
-- returned: 0 = not returned, 1 = returned
-- -------------------------------
INSERT INTO `utlån` (`member_id`, `isbn`, `eksnr`, `loan_date`, `returned`) VALUES
(1,'8203188843',1,'2022-08-25',1),
(2,'8203190483',1,'2022-08-26',0),
(3,'8203188843',2,'2022-09-02',0),
(4,'8203191543',1,'2022-09-02',1),
(5,'8203191201',1,'2022-09-06',0),
(6,'8253029533',1,'2022-09-09',0),
(7,'8274822231',1,'2022-09-11',1);