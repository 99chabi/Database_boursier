CREATE TABLE `formation` (
  `Nom de la formation` varchar(50) DEFAULT NULL,
  `Pays de formation` varchar(50) DEFAULT NULL,
  `Date de début` datetime DEFAULT NULL,
  `Date de fin` datetime DEFAULT NULL,
  `Diplôme associé` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
