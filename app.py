from flask import Flask, render_template, redirect, session
from models import connect_db, db, User, Feedback
from secrets import Key
from forms import UserForm, FeedbackForm, RegisterForm, LoginForm
from werkzeug.exceptions import Unauthorized

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flaskfdbk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = Key

connect_db(app)
db.create_all()

#user routes
@app.route('/')
def redirect_to():
    """redirect to register page"""
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """render and handle register form"""
    form = RegisterForm()
    if "username" in session:
        return redirect(f"/users/{session['username']}")
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        first_name=form.first_name.data
        last_name=form.last_name.data
        email=form.email.data

        user=User.register(username,password,first_name,last_name,email)
        db.session.commit()
        session['username']=user.username
        return redirect(f'/users/{user.username}')
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def logins():
    """render and handle login form"""
    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = LoginForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data

        user=User.authenticate(username,password)
        if user:
            session['username']=user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors=['Invalid username/password']
            return render_template("login.html", form=form)
    return render_template('login.html', form=form)

@app.route('/users/<username>')
def render_user(username):
    """render user page"""
    if "username" not in session or username != session['username']:
        raise Unauthorized()
    user=User.query.get(username)
    return render_template("render.html", user=user)

@app.route('/logout')
def logout():
    """handle logouts"""
    session.pop('username')
    return redirect('/login')

@app.route('/users/<username>/delete', methods=["POST"])
def delete_user():
    """remove user from db"""
    return

@app.route('/users/<username>/feedback/add', methods=["GET", "POST"])
def handle_new():
    """handle new feedback"""
    return 

@app.route('/feedback/<int:feedback_id>/update', methods=['GET', 'post'])
def handle_update():
    """handle updates to feedback"""
    return

@app.route('/feedback/<int:feedback_id>/delete', methods=["POST"])
def delete_feedback(feedback_id):
    """remove feedback post"""
    return