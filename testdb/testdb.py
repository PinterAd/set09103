import sqlite3
with sqlite3.connect("test.db") as db:
    cursor = db.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
        username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL);
        ''')
db.commit()
