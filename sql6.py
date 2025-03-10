# updte data

import sqlite3

db = sqlite3.connect('movies.db')
curosr = db.cursor()
curosr.execute("UPDATE movies SET title = 'The Shaw' WHERE rowid = 3 ")

curosr.execute("SELECT rowid,* FROM movies")

data = curosr.fetchall()

for row in data:
    print(row)

db.commit()
db.close()