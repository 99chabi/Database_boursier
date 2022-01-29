#!/usr/bin/python
"""
This script is made to create table in the database provided in database.ini.
The queries are provided in commands and test through try.
"""
import psycopg2
import os
import sys

from connect import config

woring_directory = "/home/e4g13/Documents/ECC/2A/S7-2021/Base_de_données/Divers/python_postgres/tables/" # Provide the working directory with all the project files.

def create_tables(directory):
    """ create tables in the PostgreSQL database from the directory containing all the SQL files """    
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        for files in os.listdir(directory):
            if files != "boursier.sql":
                print("Processing %s " % files)
                filepath = os.path.join(directory, files)
                cur.execute(open(filepath, "r").read())
                print("...done")
                
        files = "boursier.sql"
        print("Processing %s " % files)
        filepath = os.path.join(directory, files)
        cur.execute(open(filepath, "r").read())
        print("...done")
            
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
    create_tables(woring_directory)
