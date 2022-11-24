# import sqlite3
# from sqlite3 import Error 
# nie musimy koljeny raz importować sqlite3 i pisać funkcji create_connection
# możemy sobie ją zaimportować z innego pliku w tym samym folderze

from tworzenie_tabel import create_connection
# albo poniżej inna wersja tego samego importu
# import tworzenie_tabel
# tworzenie_tabel.create_connection

# def create_connection(db_file): 
#     ''' Create a database connection to the SQLite database scpecified by db_file
#     :param db_file: database file
#     :return: Connection object or None 
#     '''
#     conn = None 
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn 
#     except Error as e:
#         print(e)
#     return conn

def select_task_by_status(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param status:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE status = ?", (status,))
    rows = cur.fetchall()
    return rows

def select_all(conn, table):
    """
    Query all rows in the table
    :param conn: the Connection object
    :return:
    """    
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

def select_where(conn, table, **query):
    """
    Query tasks from table with data from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = "AND".join(qs)
    sql_query = f"SELECT * FROM {table} WHERE {q}"
    print(sql_query, values)
    cur.execute(sql_query, values)
    rows = cur.fetchall()
    return rows


conn = create_connection("database.db")

# wszytskie zadania
cur = conn.cursor()
print(cur.execute("SELECT * FROM tasks"))
rows = cur.fetchall()
print(rows)

# pobiera jedno po drugim, aż do none
cur = conn.cursor()
print(cur.execute("SELECT * FROM tasks"))
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())

# zadania ze statusem started
print(select_task_by_status(conn, 'started'))
# wszystkie projekty
print(select_all(conn, 'projects'))

query = {"nazwa":"Czasowniki regularne"}
print(select_where(conn, 'tasks', **query))
query = {"projekt_id":17}
print(select_where(conn, 'tasks', **query))

# wszytskie zadania
print(select_all(conn, "tasks"))

# wszystkie zadania dla projektu o id 21
print(select_where(conn,"tasks", projekt_id=21))

# wszystkie zadania ze statusem ended
print(select_where(conn,"tasks",status="ended"))

