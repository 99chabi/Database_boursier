import psycopg2

from config import config

def update_boursier():
 """ UPDATE boursier"""
 sql= """ set Id_boursier = %s
 set nom = %s
 set PrenomBoursier = %s
 set StatutMatrimonial = %s
 set Coordonnees = %s
 set Formation = %s
 set Bourse = %s
 set Experience_professionnelle = %s
 set Metier = %s
 set Sante = %s
 where Id_boursier = %s """
 
 conn = None
 
 print("Que voulez-vous corriger ?")
 
 
 updateded_rows = 0
 try:
  # read database configuration
  params = config()
  
  # connect to the PostgreSQL database
  conn = psycopg2.connect(**params)
  # create a new cursor
  cur = conn.cursor()
  # execute the UPDATE  statement  
  cur.execute(sql, ())
  # get the number of updated rows
  updated_rows = cur.rowcount
  # Commit the changes to the database
  conn.commit()
  # Close communication with the PostgreSQL database
  cur.close()
 except (Exception, psycopg2.DatabaseError) as error:
  print(error)
 finally:
  if conn is not None:
   conn.close()
   
   return updated_rows
  #if __name__ == '__main__':
  # Update vendor id 1
  #   update_vendor(1, "3M Corp")
  
