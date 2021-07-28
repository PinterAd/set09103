from flask import Flask, render_template, redirect, url_for, session
#from flask.helpers import url_for
#from werkzeug.utils import redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///var/database.db' 
Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')



@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
                if bcrypt.check_password_hash(user.password , form.password.data):
                    session['logged_in'] = True
                    return redirect(url_for('home'))
        return '<h1> Invalid</h1>'
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return '<h1> New user created</h1>'
    return render_template('register.html', form=form)

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)