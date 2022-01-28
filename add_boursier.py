#!usr/bin/python3

import psycopg2

from connect import config

def get_ID_statu_matrimonial():
    ID_statu_matrimonial = None
    Statut_Matrimonial = input("Statut Matrimonial : ")
    Conjoint = input("Conjoint : ")
    Enfants_à_charge = input("Enfants à charge : ")
    query = """INSERT INTO statut_matrimonial (Statut_Matrimonial, Conjoint, Enfants_à_charge) 
                VALUES (%s, %s, %s) RETURNING ID_statu_matrimonial;"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute(query, (Statut_Matrimonial, Conjoint, Enfants_à_charge))
        
        ID_statu_matrimonial = cur.fetchone()[0]
        
        # commit the changes
        conn.commit()

        # close communication with the PostgreSQL database server
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return ID_statu_matrimonial

#========================================================================================================================

def get_ID_coordonees():
    id_coordonees = None
    Adresse = input("Adresse : ")
    Mail = input("Mail : ")
    Telephone = input("Telephone : ")
    Position_actuelle = input("Position actuelle : ")

    query = """INSERT INTO coordonnées (Adresse, Mail, Telephone, Position_actuelle) 
                VALUES ( %s, %s, %s, %s) RETURNING ID_coordonees;"""

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, (Adresse, Mail, Telephone, Position_actuelle))
        # get the generated id back
        id_coordonees = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id_coordonees

#========================================================================================================================

def get_ID_formation():
    id_formation = None
    Nom_de_la_formation = input("Nom de la formation : ")
    Pays_de_formation = input("Pays de formation : ")
    Date_de_début = input("Date de début : ")
    Date_de_fin = input("Date de fin : ")
    Diplôme_associé = input("Diplôme associé : ")
    
    query = """INSERT INTO formation (Nom_de_la_formation, Pays_de_formation, Date_de_début, Date_de_fin, Diplôme_associé) 
                VALUES (%s, %s, %s, %s, %s) RETURNING ID_formation;"""

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, (Nom_de_la_formation, Pays_de_formation, Date_de_début, Date_de_fin, Diplôme_associé))
        # get the generated id back
        id_formation = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id_formation

#========================================================================================================================
   
def get_ID_bourse():
    ID_bourse = None
    Nom_de_la_bourse = input("Nom de la bourse : ")
    Montant_Alloué = int(input("Montant Alloué : "))
    Frais_de_vie = int(input("Frais de vie : "))
    Frais_de_formation = int(input("Frais de formation : "))
    Deplacement = input("Deplacement : ")
    
    query = """INSERT INTO bourse (Nom_de_la_bourse, Montant_Alloué, Frais_de_vie, Frais_de_formation, Deplacement)
                 VALUES (%s, %s, %s, %s, %s) RETURNING ID_bourse;"""
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, (Nom_de_la_bourse, Montant_Alloué, Frais_de_vie, Frais_de_formation, Deplacement))
        # get the generated id back
        ID_bourse = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return ID_bourse

#========================================================================================================================    

def get_ID_experience_pro():
    id_experience_pro = None
    PosteOccupé = input("Poste = Occupé : ")
    Durée = input("Durée : ")
    Période = input("Période : ")
    
    query = """INSERT INTO expérience_professionnelle (PosteOccupé, Durée, Période) 
                VALUES (%s, %s, %s) RETURNING ID_experience_pro;"""
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, (PosteOccupé, Durée, Période))
        # get the generated id back
        id_experience_pro = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id_experience_pro

#========================================================================================================================
    
def get_ID_metier():
    id_metier = None
    Nom_du_métier = input("Nom du métier : ")
    Salaire = int(input("Salaire : "))
    
    query = """INSERT INTO metier (Nom_du_métier, Salaire) 
                VALUES (%s, %s) RETURNING ID_metier;""" 
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, (Nom_du_métier, Salaire))
        # get the generated id back
        id_metier = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id_metier

#========================================================================================================================

def get_ID_sante():
    id_sante = None
    Sexe = input("Sexe : ") 
    Problème_de_santé = input("Problème de santé : ")
    Traitement_suivi = input("Traitement suivi : ")
    Allergies = input("Allergies : ")
    Conditions_physique = input("Conditions physique : ")
    
    query = """INSERT INTO santé (Sexe, Problème_de_santé, Traitement_suivi, Allergies, Conditions_physique) 
                VALUES (%s, %s, %s, %s, %s) RETURNING ID_sante;"""
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, (Sexe, Problème_de_santé, Traitement_suivi, Allergies, Conditions_physique))
        # get the generated id back
        id_sante = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id_sante

#========================================================================================================================

def create_boursier():
    Nom = input("Nom : ")
    PrenomBoursier = input("Prenom : ")

    ID_statu_matrimonial = get_ID_statu_matrimonial()
    Coordonnees = get_ID_coordonees()
    Formation = get_ID_formation()
    Bourse = get_ID_bourse()
    ExperienceProfessionnelle = get_ID_experience_pro()
    Metier = get_ID_metier()
    Sante = get_ID_sante()
    
    query = """INSERT INTO boursier (Nom, PrenomBoursier, ID_statu_matrimonial, Coordonnees, Formation, Bourse, ExperienceProfessionnelle, Metier, Sante) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING Id_boursier;"""
    
    id_boursier = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(query, (Nom, PrenomBoursier, ID_statu_matrimonial, Coordonnees, Formation, Bourse, ExperienceProfessionnelle, Metier, Sante))
        # get the generated id back
        id_boursier = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id_boursier

if __name__ == '__main__':
    print(create_boursier())
