import sqlite3
from sqlite3 import Error
from tworzenie_tabel import create_connection

def update(conn, table, id, **kwargs):
    """
    update status, start_data, and end_date of a task
    :param conn:
    :param table: table name
    :param id: row id
    :param kwargs: dict of attributes and values
    :return:
    """
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )
    sql = f"""UPDATE {table}
                SET {parameters}
                WHERE id =?"""
    try:
        cur=conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

if __name__ == "__main__":
    conn = create_connection("database.db")
    update(conn, "tasks", 3, status="ended")
    update(conn, "tasks", 4, stat="in progress")
    update(conn, "tasks", 4, status="in progress")
    conn.close()