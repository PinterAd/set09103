import sqlite3
with sqlite3.connect("test.db") as db:
    cursor = db.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
        username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL);
        ''')
cursor.execute('''
        INSERT INTO user(username,password)
        VALUES("newuser","456")
        ''')
db.commit()
cursor.execute("SELECT * FROM user")
print(cursor.fetchall())

