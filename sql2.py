# create tables in database

import sqlite3

con = sqlite3.connect('movies.db')

cursor = con.cursor()
cursor.execute('create table movies(title TEXT, genre TEXT, year INTEGER)')

con.commit()

con.close()