from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db=SQLAlchemy()
bcrypt=Bcrypt()

def db_connect(app):
    db.app=app
    db.init_app(app)
class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    feedback = db.relationship('Feedback', backref='user', cascade='all,delete')

    @classmethod
    def register(cls,username,password,first_name,last_name,email):
        """register user w/ hashed password"""
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8') #turn bytestring into normal unicode utf8 string
        
        user = cls(username=username,password=hashed_utf8,first_name=first_name,last_name=last_name,email=email)
        db.session.add(user)

        return user #return instance of user

    @classmethod
    def auth(cls,username,password):
        """VALIDATE USER EXISTENCE AND IF PASSWORD MATCHES USER"""
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, password):
            #if valid return instance of user
            return u
        else:
            #else return false
            return False

class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('users.username'), nullable=False)