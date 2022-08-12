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
