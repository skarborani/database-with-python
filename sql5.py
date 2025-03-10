#read data from the table

import sqlite3

db = sqlite3.connect('movies.db')

cursor = db.cursor()
data = cursor.execute("SELECT rowid,* FROM movies")
data = cursor.fetchall()

for row in data:
    print(row)


db.commit()
db.close()