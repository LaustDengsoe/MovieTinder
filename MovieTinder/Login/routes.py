from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from MovieTinder.forms import UserLoginForm
from MovieTinder.models import select_User
from MovieTinder import bcrypt

Login = Blueprint('Login', __name__)

@Login.route("/")
def frontpage():
    return render_template('frontpage.html')

@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))

    form = UserLoginForm()
    if form.validate_on_submit():
        user = select_User(form.username.data)
        print(user)
        if user != None and bcrypt.check_password_hash(user[2], form.password.data):
            login_user(user)
            return redirect(url_for('Login.home'))
        else:
            flash('Login unsuccessful. Please check the username and password', 'danger')

    return render_template('login.html', form = form)

@Login.route("/register")
def register():
    return render_template('register.html')

@Login.route("/home")
@login_required
def home():
    return render_template('home.html')