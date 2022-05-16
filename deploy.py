import sqlite3, os
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute('pragma foreign_keys = ON;')
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def createDB(con):
    # declare tables
    personen = """CREATE TABLE IF NOT EXISTS personen (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    voornaam text not null,
                    tussenvoegsel text,
                    achternaam text not null,
                    email text not null,
                    code_functie text,
                    sts_rec integer
    );"""

    functies = """CREATE TABLE IF NOT EXISTS functies (
                    code_functie text PRIMARY KEY,
                    functie text not null,
                    sts_rec integer
    );"""

    applicaties = """CREATE TABLE IF NOT EXISTS applicaties (
                    code_applicatie text PRIMARY KEY,
                    applicatie text not null,
                    sts_rec integer
    );"""

    # create tables in database
    create_table(create_connection(con), personen)
    create_table(create_connection(con), functies)
    create_table(create_connection(con), applicaties)        
        
