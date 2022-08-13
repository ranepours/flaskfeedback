from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)])
    first_name=StringField("First Name", validators=[InputRequired(), Length(max=30)])
    last_name=StringField("Last Name", validators=[InputRequired(), Length(max=30)])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])

class UserForm(FlaskForm):
    username=StringField("Username", validators=[InputRequired()])
    password=PasswordField("Password", validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    content = StringField("Feedback Text", validators=[InputRequired()])
    title = StringField("Title", validators=[InputRequired(), Length(max=100)])