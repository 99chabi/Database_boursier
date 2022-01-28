CREATE TABLE expérience_professionnelle (
  ID_experience_pro SERIAL,
  PosteOccupé varchar(1024) DEFAULT NULL,
  Durée varchar(1024) DEFAULT NULL,
  Période varchar(1024) DEFAULT NULL,
  UNIQUE(ID_experience_pro)
);

-- Handle experiences by providing them in an arrows and handle the output later in the developpement.
