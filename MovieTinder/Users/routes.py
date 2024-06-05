from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from flask_login import login_required, current_user, logout_user
from MovieTinder.forms import UserChangeNameForm, UserChangePassForm, UserMovieReactForm, UserSearchForm, UserFriendRemoveMatchForm
from MovieTinder.models import select_User, update_Username, update_Pass, select_new_Movie, insert_Like, select_Friends, select_Users_Search
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

@Users.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    movie = select_new_Movie(current_user[0])
    poster = f'static/images/posters/poster_{movie.imdb_id}.jpg' if movie != None else None

    react_form = UserMovieReactForm()
    if react_form.validate_on_submit():
        if react_form.like.data:
            insert_Like(current_user[0], session['movie_id'])
        elif react_form.dislike.data:
            print('dislike')
        return redirect(url_for('Users.home'))

    
    session['movie_id'] = movie.id if movie != None else None

    return render_template('home.html', image_src = poster, movie=movie, form = react_form)

@Users.route("/friends", methods=['GET', 'POST'])
@login_required
def friends():
    
    search_form = UserSearchForm()
    search_query = request.args.get('search')
    if search_query:
        users = select_Users_Search(current_user[0], f'^{search_query}.*')
    else:
        users = None

    remove_match_form = UserFriendRemoveMatchForm()
    if remove_match_form.validate_on_submit():
        if remove_match_form.remove.data:
            print(remove_match_form.user_id.data)
        elif remove_match_form.matches.data:
            print(f'Matches {remove_match_form.user_id.data}')

        return redirect(url_for('Users.friends'))    
    
    friends = select_Friends(current_user[0])
    return render_template('friends.html', friends=friends, form=search_form, users=users, friend_form=remove_match_form)

@Users.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('Login.frontpage'))