from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from MovieTinder.forms import UserLoginForm, UserRegisterForm
from MovieTinder.models import select_User, insert_User
from MovieTinder import bcrypt

Login = Blueprint('Login', __name__)

@Login.route("/")
def frontpage():
    return render_template('frontpage.html')

@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Users.home'))

    form = UserLoginForm()
    if form.validate_on_submit():
        user = select_User(form.username.data)
        if user != None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('Users.home'))
        else:
            flash('Login unsuccessful. Please check the username and password', 'danger')

    return render_template('login.html', form = form)

@Login.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('Users.home'))

    form = UserRegisterForm()
    if form.validate_on_submit():
        user = select_User(form.username.data)
        if user != None:
            flash('Username already taken!', 'danger')
            user = None
        else:
            if form.password.data == form.password_confirmed.data:
                username = form.username.data
                password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                insert_User(username, password)
                user = select_User(username)
                login_user(user)
                return redirect(url_for('Users.home'))
            else:
                flash('Passwords do not match!', 'danger')

    return render_template('register.html', form = form)