CREATE TABLE bourse (
  ID_bourse SERIAL,
  Nom_de_la_bourse varchar(1024) NOT NULL DEFAULT '',
  Montant_Alloué int DEFAULT NULL,
  Frais_de_vie int DEFAULT NULL,
  Frais_de_formation int DEFAULT NULL,
  Deplacement varchar(1024) DEFAULT NULL,
  PRIMARY KEY (ID_bourse),
  UNIQUE(ID_bourse)
);

