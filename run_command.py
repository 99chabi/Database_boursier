#!/usr/bin/python


"""
Script from : ~/Documents/ECC/2A/S7-2021/Base_de_données/Divers/Database_boursier
Here we run a command from a string provided by the user
Update the current folder's script
"""

import psycopg2

from connect import config

def run_command(user_query):
    """ create tables in the PostgreSQL database"""
    #commands = (""" SELECT * FROM vendors """)
    #commands = user_query
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # create table one by one
        for query in user_query:
            cur.execute(query)
        #cur.execute('SELECT * from vendors')
        
        # Fetch the output
        result = cur.fetchall()
        
        #print(result[0])
        # display each records from the tuple result. The return is automatically made
        for i in range(0, len(result)):
            print(result[i])
        #print("\n")
        # close communication with the PostgreSQL database server
        cur.close()
        
        # commit the changes
        conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    run_command('SELECT * from vendors')
