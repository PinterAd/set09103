from flask import Flask, redirect, url_for

app = Flask(__name__)

    # def pages
@app.route('/')
def root():
    return "Default, 'root' route "

@app.route("/hello/")
def hello():
    return "Hello Napier!"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world :("

@app.route("/private/")
def private():
    return redirect(url_for("login"))
        
    # redirect for private
@app.route("/login")
def login():
    return "Login page"
    
    # custom 404
@app.errorhandler(404)
def page_not_found(error):
    return "Nothing to see here.", 404
    
    # force 404
@app.route("/force404/")
def force404():
    abort(404)
    
    # static image
@app.route("/static-example/img")
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename='vmask.jpg')
    end = '">'
    return start+url+end, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

