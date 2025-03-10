import sqlite3
con = sqlite3.connect('movies.db')
cursor = con.cursor()

movies = [
    ('the godfather', 'crime', 1970),
    ('fast 9', 'action', 2020),
    ('the whale', 'drama', '2023'),
    ('delete history', 'comedy', 2021),
    ('Apples', 'fantasy', '2019'),
    ('nomadland', 'drama', 2018),
]

cursor.executemany("INSERT INTO movies VALUES(?,?,?)", movies)
con.commit()
con.close()

