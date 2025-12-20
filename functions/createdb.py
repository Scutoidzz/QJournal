import sqlite3 as sql


def create_database():
    try:
        conn = sql.connect("qjournal.db")
    except sql.Error as e:
        print(e)
        