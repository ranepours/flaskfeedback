from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db=SQLAlchemy()
bcrypt=Bcrypt()

def connect_db():
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    feedback = db.relationship('Feedback', backref='user', cascade='all,delete')

class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('users.username'), nullable=False)