from flask import Flask
from flask import render_template
from flask import request
import dbtest as dbHandler

app= Flask(__name__)

@app.route('/login.html', methods=['POST', 'GET'])
def login():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		dbHandler.insertUser(username, password)
   		users = dbHandler.retrieveUsers()
		return render_template('Noteshare.html', users=users)
   	else:
   		return render_template('Noteshare.html')


@app.route('/')
def root():
    return render_template('Noteshare.html')

@app.route('/Noteshare.html')
def noteshare():
    return render_template('Noteshare.html')

@app.route('/forum.html')
def forum():
    return render_template('forum.html')

@app.route('/qa.html')
def qa():
    return render_template('qa.html')

@app.route('/topics.html')
def topics():
    return render_template('topics.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
