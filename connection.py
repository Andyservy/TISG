import sqlite3

import os

path = os.path.abspath('boost_mannager.db')

_connection = sqlite3.connect(path)


def connection():

    return _connection