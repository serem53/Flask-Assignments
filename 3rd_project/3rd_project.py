#. Implement user authentication and registration in a Flask app using Flask-Login.

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Ensure the app context is pushed so that db.create_all() works
with app.app_context():
    # Create the database tables
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
         username = request.form['username']
         password = request.form['password']

         # Check if the username already exists
         if User.query.filter_by(username=username).first():
            return render_template('signup.html', message='Username already exists. Please choose a different one.')

         # Create a new user
         new_user = User(username=username,password=password)
         

     # Add the new user to the database
         db.session.add(new_user)
         db.session.commit()

    # Redirect to  home page
         return redirect(url_for('home'))

    return render_template('signup.html')





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)