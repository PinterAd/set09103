from flask import Flask , render_template
app= Flask(__name__)

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
