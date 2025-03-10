#insert row into table

import sqlite3
con = sqlite3.connect('movies.db')

cursor = con.cursor()
cursor.execute("INSERT INTO movies VALUES('oppenheimer','drama', 2023)")

con.commit()
con.close()