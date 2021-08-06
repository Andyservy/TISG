import mysql.connector

_connection = None


def connection():
    global _connection
    if not _connection:
        _connection = mysql.connector.connect(host="127.0.0.1", user="root", password="76743571mysql",
                                              database="boost_mannager")
    return _connection


def column_name(name):
    # This is meant to mostly do the same thing as the _process_params method
    # of mysql.connector.MySQLCursor, but instead of the final quoting step,
    # we escape any previously existing backticks and quote with backticks.
    converter = mysql.connector.conversion.MySQLConverter()
    return "`" + converter.escape(converter.to_mysql(name)).replace('`', '``') + "`"
