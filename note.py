from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///var/users.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(26), unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)

class RegistrationForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=26)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def validate_username(self,username):
        check_user = UserInfo.query.filter_by(username=username.data).first()
        if check_user:
            raise ValidationError('Username taken')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=26)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route("/")
def root():
    return render_template('Noteshare.html')
    
@app.route("/home")
def home():
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

@app.route("/register.html" , methods=['GET' , 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_data = UserInfo(username=form.username.data , password=password_hash)
        db.session.add(user_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html' , form=form)

@app.route("/login.html" , methods=['GET' , 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = UserInfo.query.filter_by(username=form.username.data).first()
        validate_pass = bcrypt.check_password_hash(username.password , form.password.data)
        
        if username and validate_pass:
            flash(f'Login succesful!')
            return redirect(url_for('home'))
        else:
            flash(f'Invalid password!')
            return redirect(url_for('home'))
    return render_template('login.html' , form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)