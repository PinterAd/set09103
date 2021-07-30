from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/display/')
def display():
    return '<embed src="'+url_for('static', filename='uploads/file.pdf')+'" type="application/pdf" width="100%" height="100%" />'

@app.route('/upload/', methods=['POST','GET'])
def account():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/' + filename + '.pdf')
        return "File Uploaded"
    else:
        page='''
        <html>
        <body>
        <form action="" method="post" name="form" enctype="multipart/form-data">
        <input type="file" name="datafile" />
        <input type="submit" name="submit" id="submit"/>
        </form>
        </body>
        </html>
        '''
        return page, 200
    if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)
