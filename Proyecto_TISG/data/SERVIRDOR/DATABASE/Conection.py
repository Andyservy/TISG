import mysql.connector

_connection = None


def connection():
    global _connection
    if not _connection:
        _connection = mysql.connector.connect(host="127.0.0.1", user="root", password="76743571mysql",
                                              database="boost_mannager")
    return _connection
