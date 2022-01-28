CREATE TABLE santé (
  ID_sante SERIAL,
  Sexe varchar(1024) DEFAULT NULL,
  Problème_de_santé varchar(1024) DEFAULT NULL,
  Traitement_suivi varchar(1024) DEFAULT NULL,
  Allergies varchar(1024) DEFAULT NULL,
  Conditions_physique varchar(1024) DEFAULT NULL,
  UNIQUE(ID_sante)
);
