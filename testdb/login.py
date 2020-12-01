import sqlite3
def login():
    while True:
        username = input("username: ")
        password = input("password: ")
        with sqlite3.connect("test.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()
        if results:
            for i in results:
                print("welcome"+i[1])
            #return("exit")
                break

        else:
            print("NOPE")
            again = input("try again? (y/n)  ")
            if again.lower() == "n":
                print("goodbye")
               # return("exit")
                break
login()

