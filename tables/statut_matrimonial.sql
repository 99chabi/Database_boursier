CREATE TABLE statut_matrimonial (
  ID_statu_matimonial SERIAL,
  Statut_Matrimonial varchar(1024) DEFAULT NULL,
  Conjoint varchar(1024) DEFAULT NULL,
  Enfants_à_charge varchar(1024) DEFAULT NULL,
  UNIQUE(ID_statu_matimonial)
);
-- We need to provide all availavable cases.
