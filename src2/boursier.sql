CREATE TABLE `boursier` (
  `Id_boursier` int NOT NULL,
  `Nom` varchar(50) DEFAULT NULL,
  `PrenomBoursier` varchar(50) DEFAULT NULL,
  `StatutMatrimonial` varchar(50) DEFAULT NULL,
  `Coordonnees` varchar(50) DEFAULT NULL,
  `Formation` varchar(50) DEFAULT NULL,
  `Bourse` varchar(50) DEFAULT NULL,
  `ExperienceProfessionnelle` varchar(50) DEFAULT NULL,
  `Metier` varchar(50) DEFAULT NULL,
  `Sante` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id_boursier`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
