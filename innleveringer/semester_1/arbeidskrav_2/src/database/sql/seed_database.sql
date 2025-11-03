-- -------------------------------
-- This file inserts example data into the library database tables.
-- Order of inserts: bok → eksemplar → låner → utlån
-- -------------------------------

-- -------------------------------
-- Insert example books
-- -------------------------------
INSERT INTO `bok` (`ISBN`, `Tittel`, `Forfatter`, `Forlag`, `UtgittÅr`, `AntallSider`) VALUES
('8203188443','Kristin Lavransdatter: kransen','Undset, Sigrid','Aschehoug',1920,323),
('8203209394','Fyret: en ny sak for Dalgliesh','James, P. D.','Aschehoug',2005,413),
('8250312443','Lasso rundt fru Luna','Mykle, Agnar','Gyldendal',1954,614),
('8205336148','Victoria','Hamsun, Knut','Gyldendal',1898,111),
('8253025033','Jonas','Bjørneboe, Jens','Pax',1955,302),
('8274842231','Den gamle mannen og havet','Hemingway, Ernest','Gyldendal',1952,99);

-- -------------------------------
-- Insert copies of books
-- -------------------------------
INSERT INTO `eksemplar` (`ISBN`, `EksNr`) VALUES
('8203188443',1),
('8203188443',2),
('8203209394',1),
('8250312443',1),
('8250312443',2),
('8205336148',1),
('8253025033',1),
('8274842231',1);

-- -------------------------------
-- Insert library members
-- -------------------------------
INSERT INTO `låner` (`Fornavn`, `Etternavn`, `Adresse`) VALUES
('Lise','Jensen','Erling Skjalgssons gate 56'),
('Joakim','Gjertsen','Grinda 2'),
('Katrine','Garvik','Ottar Birtings gate 9'),
('Emilie','Marcussen','Kyrre Grepps gate 19'),
('Valter','Ellersten','Fyrstikkbakken 5D'),
('Tormod','Vakdsal','Lassons gate 32'),
('Asle','Eckhoff','Kirkeveien 5'),
('Birthe','Aass','Henrik Wergelands Allé 47');

-- -------------------------------
-- Insert loans
-- -------------------------------
INSERT INTO `utlån` (`LNr`, `ISBN`, `EksNr`, `Utlånsdato`, `Levert`) VALUES
(2,'8203209394',1,'2022-08-25',0),
(1,'8253025033',1,'2022-08-25',1),
(3,'8203188443',1,'2022-09-02',0),
(4,'8274842231',1,'2022-09-02',1),
(5,'8205336148',1,'2022-09-02',0),
(6,'8253025033',1,'2022-09-09',0),
(7,'8250312443',1,'2022-09-11',1);
