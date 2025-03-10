import sqlite3

db = sqlite3.connect('movies.db')
curosr = db.cursor()


curosr.execute("DELETE FROM movies WHERE title = 'delete history'")

curosr.execute("SELECT rowid,* FROM movies")

data = curosr.fetchall()

for row in data:
    print(row)

db.commit()
db.close()