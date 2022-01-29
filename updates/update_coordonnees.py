import psycopg2
from config import config

def update_coordonnees():
    """ UPDATE coordonnees"""
    sql= """ set ID_coordonnees = %s
    set addresse = %s
    set mail = %s
    set telephone = %s
    set position actuelle = %s
    where ID_coordonnees = %s """
    conn = None
    
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
        
