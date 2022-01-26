CREATE TABLE `bourse` (
  `Nom de la bourse` varchar(50) NOT NULL DEFAULT '',
  `Montant Alloué` int DEFAULT NULL,
  `Frais de vie` int DEFAULT NULL,
  `Frais de formation` int DEFAULT NULL,
  `Deplacement` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Nom de la bourse`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

