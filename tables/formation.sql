CREATE TABLE formation (
  ID_formation SERIAL,
  Nom_de_la_formation varchar(1024) DEFAULT NULL,
  Pays_de_formation varchar(1024) DEFAULT NULL,
  Date_de_début date DEFAULT NULL,
  Date_de_fin date DEFAULT NULL,
  Diplôme_associé varchar(1024) DEFAULT NULL,
  UNIQUE(ID_formation)
);
