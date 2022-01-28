CREATE TABLE déplacement (
  ID_deplacement SERIAL,
  Moyen_de_déplacement varchar(1024) NOT NULL DEFAULT '',
  Frais_de_déplacement int DEFAULT NULL,
  Date_de_départ date DEFAULT NULL,
  Date_d_arrivée date DEFAULT NULL,
  PRIMARY KEY (Moyen_de_déplacement),
  UNIQUE(ID_deplacement)
);
