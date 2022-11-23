import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    ''' Create a database connection to the SQLite database scpecified by db_file
    :param db_file: database file
    :return: Connection object or None 
     '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Connected to {db_file}, sqlite version: {sqlite3.version}')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r"my_database.db")