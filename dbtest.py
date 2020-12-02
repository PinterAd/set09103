import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("test.db")
    cur = con.cursor()
    cur.execute("INSERT INTO user (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("test.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM user")
	users = cur.fetchall()
	con.close()
	return user
