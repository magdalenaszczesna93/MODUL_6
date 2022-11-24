import sqlite3
from sqlite3 import Error
from tworzenie_tabel import create_connection

# DELETE FROM <nazwa tabeli> usuwa wszystkie wpisy z jakiejś tabeli
# DELETE FROM tasks WHERE id=3, usuwa zadanie o id=3

def delete_where(conn, table, **kwargs):
    """
    Delete from table where attributes from
    :param conn: Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values
    :return:
    """
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = "AND".join(qs)
    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Deleted")

# def delete_all(conn, table):
#     """
#     Delete all rows from table
#     :param conn: Connection to the SQLite database
#     :param table: table name
#     :return:
#     """
#     sql = f'DELETE FROM {table}'
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()
#     print("Deleted")

if __name__ == "__main__":
    conn = create_connection("database.db")
    print(delete_where(conn, "tasks", id=20))
    # print(delete_all(conn,"tasks"))
