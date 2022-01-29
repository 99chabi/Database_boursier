-- This query is for filling the Statut_matrimonial table
INSERT INTO statut_matrimonial (Statut_Matrimonial, Conjoint, Enfants_à_charge)
VALUES ('Célibataire', 'Aucun', '0');

--This query is for filling coordonnees table
INSERT INTO coordonnees (Adresse, Mail, Telephone, Position_actuelle)
VALUES ('Bouskoura, Maroc', 'ayodele.ogodja@centrale-casablanca.ma', '+212623873311', 'Chez lui');

-- This query is for filling the formation table
INSERT INTO formation (Nom_de_la_formation, Pays_de_formation, Date_de_début, Date_de_fin, Diplôme_associé)
VALUES ('Centralienne', 'Maroc', '15 Septembre 2020', '30 Juillet 2024', 'Ingénieur Centralien');

-- This query is for filling the bourse table
INSERT INTO bourse (Nom_de_la_bourse, Montant_Alloué, Frais_de_vie, Frais_de_formation, Deplacement)
VALUES ('IMA Excellence & Leadership', '4300', '2000', '4000', 'Avion');

-- This query is for filling the experience professionnelle
INSERT INTO expérience_professionnelle (PosteOccupé, Durée, Période)
VALUES ('CEO', '7ans', '2025-2030');

-- This query is for filling the metier table
INSERT INTO metier (Nom_du_métier, Salaire)
VALUES ('Ingénieur', '52000');

-- This query is for filling the santé table
INSERT INTO santé (Sexe, Problème_de_santé, Traitement_suivi, Allergies, Conditions_physique)
VALUES ('30cm', 'Aucun', 'Aucun', 'Aucune', 'Ready for deployment');

-- This query is for adding an new boursier to the database
INSERT INTO boursier (Nom, PrenomBoursier)
VALUES ('Joseph', 'OGODJA');
