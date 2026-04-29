import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

cur.execute("""
INSERT INTO users (username, password)
VALUES ('admin', 'supersecret123')
""")

conn.commit()
conn.close()

print("Database created successfully")