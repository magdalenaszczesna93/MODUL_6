# ex_02_create_tables.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file): 
    ''' Create a database connection to the SQLite database scpecified by db_file
    :param db_file: database file
    :return: Connection object or None 
    '''
    conn = None  # Obiekt połączenia, jak się nie wykona try, to wraca do pierwszej wartości None
    try:
        conn = sqlite3.connect(db_file)
        return conn
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

def add_project(conn, project): # Jak ta funkcja się wywołuje, skoro nie jest wywołana niżej ? 
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO projects(nazwa, start_date, end_date)
                VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def add_task(conn, task):
    """
    Create a new task into the task table
    :param conn:
    :param task:
    :return: task id
    """
    sql = '''INSERT INTO tasks(projekt_id, nazwa, opis, status, start_data, end_date)
        VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid
print(__name__)

if __name__ == '__main__': # Do uruchamiania bezpośredniego
    
    create_projects_sql = """
    -- projects table
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        nazwa text NOT NULL,
        start_date text,
        end_date text);
    """   
    create_tasks_sql = """
    -- zadanie table
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        projekt_id integer NOT NULL,
        nazwa VARCHAR(250) NOT NULL,
        opis TEXT,
        status VARCHAR(15) NOT NULL,
        start_data text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (projekt_id) REFERENCES projects (id));
    """

    db_file = "database.db"
    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn,create_projects_sql)
        execute_sql(conn, create_tasks_sql)
        conn.close()
    # to powyżej otwiera połącznie do database.db tworzy tabele i zamyka połączenie

    conn = create_connection("database.db")

    project = ("Pompki", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
    pr_id = add_project(conn, project) # wywołuję funkcję add_project

    task = (
        pr_id,
        "Czasowniki regularne",
        "Zapamiętaj czasowniki ze strony 30",
        "ended",
        "2020-05-11 12:00:00",
        "2020-05-11 15:00:00")
    task_id = add_task(conn, task) #wywołuję funkcję add_task

    print(pr_id, task_id)
    conn.commit() # Zapisuje bazę

