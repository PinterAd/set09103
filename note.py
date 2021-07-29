from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///var/database.db' 
Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))
    files = db.relationship('File', backref='uploader')

class File(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(20))
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class UploadForm(FlaskForm):
    filename = StringField('Filename', validators=[InputRequired()])

@app.route('/home')
def home():
    files = File.query.all()
    return render_template('index.html', files=files)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
                if bcrypt.check_password_hash(user.password , form.password.data):
                    session['logged_in'] = True
                    login_user(user)
                    return redirect(url_for('home'))
        return '<h1> Invalid</h1>'
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

@app.route('/logout')
#@login_required
def logout():
    logout_user()
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/upload', methods=['GET', 'POST'])
#@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        
            filename = form.filename.data
            f = request.files['datafile']
            f.save('static/uploads/' + filename + '.pdf')

            new_file = File(filename=form.filename.data, uploader=current_user)
            db.session.add(new_file)
            db.session.commit()
            
            flash('Document uploaded successfully.')
    return render_template('upload.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)