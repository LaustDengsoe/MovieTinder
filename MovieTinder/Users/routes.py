from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from flask_login import login_required, current_user, logout_user
from MovieTinder.forms import *
from MovieTinder.models import *
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
        movie_id = request.form.get('movie_id')
        if react_form.like.data:
            insert_Like(current_user[0], movie_id)
        elif react_form.dislike.data:
            insert_Dislike(current_user[0], movie_id)
            
        return redirect(url_for('Users.home'))

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

    remove_form = UserRemoveFriendForm()
    add_form = UserAddFriendForm()
    if 'form_name' in request.form:
        if request.form['form_name'] == 'remove_match_form' and remove_form.validate():
            friend_id = request.form.get('user_id')
            if remove_form.remove.data:
                delete_Friend(current_user[0], friend_id)
            return redirect(url_for('Users.friends'))  
        
        elif request.form['form_name'] == 'add_form' and add_form.validate():
            add_id = request.form.get('add_id')
            if add_form.add.data:
                insert_Friend(current_user[0], add_id)
            return redirect(url_for('Users.friends'))  

    friends = select_Friends(current_user[0])
    return render_template('friends.html', friends=friends, form=search_form, users=users,
                           remove_form=remove_form, add_form = add_form)

@Users.route("/matches", methods=['GET', 'POST'])
@login_required
def matches():
    friends = select_Friends(current_user[0])
    matches_form = UserSeeMatchesForm ()
    if 'form_name' in request.form:
        if request.form['form_name'] == 'matches_form' and matches_form.validate():
            friend_id = request.form.get('user_id')
            if matches_form.see_matches.data:
                session['friend'] = select_Friend(friend_id)
                session['movies'] = select_common_Movies(current_user[0], friend_id)
            return redirect(url_for('Users.matches'))  

    friend = User(session['friend']) if session.get('friend') != None else None
    movies = [Movie(movie) for movie in session.get('movies')] if session.get('movies') != None else None
    return render_template('matches.html', friends=friends, matches_form=matches_form,
                           match_friend = friend, movies=movies)

@Users.route("/likes", methods=['GET', 'POST'])
@login_required
def likes():
    movies = select_all_liked_movies(current_user[0]) 
    print(movies)
        
    return render_template('likes.html', movies=movies)


@Users.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('Login.frontpage'))