from flask import Flask, render_template, redirect
from secrets import SECRET
from models import connect_db, db, User, Feedback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flaskfdbk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = SECRET

connect_db(app)
db.create_all()

#user routes
@app.route('/')
def redirect_to():
    """redirect to register page"""
    return redirect()

@app.route('/register', methods=['GET', 'POST'])
def register():
    """render and handle register form"""
    return

@app.route('/login', methods=['GET', 'POST'])
def logins():
    """render and handle login form"""
    return

@app.route('/secret')
def secrets():
    return "<h1>You made it</h1>"

#feedback routes