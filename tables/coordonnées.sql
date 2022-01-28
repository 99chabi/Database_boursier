CREATE TABLE coordonnées (
  ID_coordonees SERIAL,
  Adresse varchar(1024) DEFAULT NULL,
  Mail varchar(1024) DEFAULT NULL,
  Telephone int DEFAULT NULL,
  Position_actuelle varchar(1024) DEFAULT NULL,
  UNIQUE(ID_coordonees)
);
