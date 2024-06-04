from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from MovieTinder.forms import UserChangeNameForm, UserChangePassForm
from MovieTinder.models import select_User, update_Username, update_Pass
from MovieTinder import bcrypt

Users = Blueprint('Users', __name__)

@Users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    username_form = UserChangeNameForm()
    pass_form = UserChangePassForm()
    
    if username_form.validate_on_submit():
        new_username = username_form.username.data
        new_username_confirmed = username_form.username_confirmed.data
        if new_username == new_username_confirmed:
            if select_User(new_username) != None:
                flash('Username is already taken!', 'danger')
            else:
                update_Username(current_user[0], new_username)
                flash('Username has been updated!', 'success')

        else:
            flash('Usernames do not match!', 'danger')

    if pass_form.validate_on_submit():
        new_pass = pass_form.password.data
        new_pass_confirmed = pass_form.password_confirmed.data
        if new_pass == new_pass_confirmed:
            new_pass = bcrypt.generate_password_hash(new_pass).decode('utf-8')
            update_Pass(current_user[0], new_pass)
            flash('Password has been updated!', 'success')
        else:
            flash('Passwords do not match!', 'danger')

    return render_template('account.html', username_form = username_form, pass_form = pass_form)