import mysql.connector


def con_db():
    return mysql.connector.connect(
        host="localhost",
        database="db_teste",
        user="root",

        passwd="123456"
    )