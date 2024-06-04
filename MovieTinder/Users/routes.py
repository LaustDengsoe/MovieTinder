from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from flask_login import login_required, current_user
from MovieTinder.forms import UserChangeNameForm, UserChangePassForm, UserMovieReactForm, UserSearchForm
from MovieTinder.models import select_User, update_Username, update_Pass, select_new_Movie, insert_Like, select_Friends, select_Users
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
    poster = f'static/images/posters/poster_{movie.imdb_id}.jpg'
    title = movie.title
    year = movie.year
    summary = movie.summary

    react_form = UserMovieReactForm()
    if react_form.validate_on_submit():
        if 'like' in request.form:
            insert_Like(current_user[0], session['movie_id'])
        elif 'dislike' in request.form:
            print('dislike')
        return redirect(url_for('Users.home'))

    session['movie_id'] = movie.id

    return render_template('home.html', image_src = poster, movie_title = title, movie_year = year,
                            movie_summary = summary, form = react_form)

@Users.route("/friends", methods=['GET', 'POST'])
@login_required
def friends():
    
    search_form = UserSearchForm()
    search_query = request.args.get('search')
    if search_query and len(search_query) >= 4:
        print('Search!')
    
    friends = select_Friends(current_user[0])
    return render_template('friends.html', friends=friends, form=search_form)

