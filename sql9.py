import sqlite3

db = sqlite3.connect('movies.db')
cur = db.cursor()

cur.execute('DROP TABLE users')
# Fixing the table creation statement
cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )""")  # Removed the extra comma

cur.execute("INSERT INTO users (age) VALUES (31)")
cur.execute("SELECT * FROM users")
data = cur.fetchall()
for row in data:
    print(row)

db.commit()
db.close()
