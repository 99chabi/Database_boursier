CREATE TABLE metier (
  ID_metier SERIAL,
  Nom_du_métier varchar(1024) DEFAULT NULL,
  Salaire int DEFAULT NULL,
  UNIQUE(ID_metier)
);
