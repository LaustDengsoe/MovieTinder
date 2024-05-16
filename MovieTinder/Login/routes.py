from flask import Blueprint, render_template
from MovieTinder.forms import UserLoginForm

Login = Blueprint('Login', __name__)

@Login.route("/")
def frontpage():
    return render_template('frontpage.html')

@Login.route("/login")
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        1
    return render_template('login.html')

@Login.route("/register")
def register():
    return render_template('register.html')