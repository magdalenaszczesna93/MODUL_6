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
    # finally:
    #     if conn:
    #         conn.close()

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
    :param conn: Connection object
    :param subject: subject name
    :return: print("added")
    """
    sql = '''INSERT INTO subjects(name_subject, teacher)
                VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, subject)
    conn.commit()
    print("Added")

def add_student(conn, student):
    """
    Create a new task into the students table
    :param conn: Connection object
    :param student: student data
    :return: print("added")
    """
    sql = '''INSERT INTO students(subject_id, name, surname, year_of_study, subject_grade)
        VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    print("Added")

    # pobieranie wszytskiego z subjects
def select_all(conn, table):
    """ Query all rows in the table :param conn: the Connection object :return: """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

    # wyszukuje po subject grade and subject id
def select_students_by_grade(conn, subject_grade, subject_id):
    """ Query sudents by subject_grade :param conn: the Connection opbject :param subject_grade: subject_grade 
    :param subject_id: subject_id :return: """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM students WHERE subject_grade=? AND subject_id=?",(subject_grade,subject_id))
    rows = cur.fetchall()
    return rows


if __name__ == '__main__':
    # wykonano
    # Tworzę połączenie z bazą, chyba że nie istneije to tworzy z podaną nazwą
    # create_connection(r"my_database.db")  

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
    # wykonano
    # conn = create_connection("my_database.db")
    # tworzę tabelę
    # if conn is not None: 
    #     execute_sql(conn,create_subjects_sql)
    #     execute_sql(conn,create_students_sql)
    #     conn.close()

    conn = create_connection("my_database.db") #połączenie z bazą

    # wykoanno
    # subject = ("Geaografia", "W. O'Conor")
    # add_subject(conn, subject) # wywołuję funkcję add_subject

    # wykonano
    # student = (6, "Eric", "Goldman", 2, 5)
    # add_student(conn, student) # wywołuję funkcję add_student

    # pobiera wszytsko z sebject
    print(select_all(conn, "subjects"))

    # pobiera po kolei ze students
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    print(cur.fetchone())
    print(cur.fetchone())
    print(cur.fetchone())
    
    print(select_students_by_grade(conn, 5, 1))