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
    return conn

def execute_sql(conn, sql): # sql - tekst, kod sql, który jest podany do zmiennej 
    #przekzanej do funkcji
    ''' Execute sql
    :param conn: Connection object
    :param sql: a Sql script
    :return:
    '''
    try:
        c = conn.cursor() 
        c.execute(sql)
    except Error as e:
        print(e)

def add_subject(conn, subject): 
    """
    Create a new project into the subjects table
    :param conn:
    :param subject: subject name
    :return: subject id
    """
    sql = '''INSERT INTO subjects(name_subject, teacher)
                VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, subject)
    conn.commit()
    print("Added")

if __name__ == '__main__':
    
    create_subjects_sql = """
    -- subject table
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name_subject VARCHAR(50) NOT NULL,
        teacher TEXT);
    """   
    create_students_sql = """
    -- student table
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        subject_id INTEGER NOT NULL,
        name VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        year_of_study INTEGER NOT NULL,
        subject_grade FLOAT NOT NULL,
        FOREIGN KEY (subject_id) REFERENCES subjects (id));
    """
    conn = create_connection("my_database.db")
    if conn is not None:
        execute_sql(conn,create_subjects_sql)
        execute_sql(conn,create_students_sql)
        conn.close()

    conn = create_connection("my_database.db")

    subject = ("Geaografia", "W. O'Conor")
    add_subject(conn, subject) # wywołuję funkcję add_subject