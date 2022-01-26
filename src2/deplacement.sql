CREATE TABLE `déplacement` (
  `Moyen de déplacement` varchar(50) NOT NULL DEFAULT '',
  `Frais de déplacement` int DEFAULT NULL,
  `Date de départ` datetime DEFAULT NULL,
  `Date d'arrivée` datetime DEFAULT NULL,
  PRIMARY KEY (`Moyen de déplacement`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
