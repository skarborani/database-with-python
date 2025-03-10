import sqlite3

db = sqlite3.connect('movies.db')

cursor = db.cursor()

cursor.execute("INSERT INTO movies VALUES ('SALT', 'action', 2017)")


cursor.execute('SELECT rowid,* FROM movies')
data = cursor.fetchall()
for row in data:
    print(row)

db.commit()
db.close()
