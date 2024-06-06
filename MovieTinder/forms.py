from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SearchField, HiddenField
from wtforms.validators import DataRequired

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UserRegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirmed = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register Me!')

class UserChangeNameForm(FlaskForm):
    username = StringField('New username', validators=[DataRequired()])
    username_confirmed = StringField('Confirm new username', validators=[DataRequired()])
    submit = SubmitField('Update username')

class UserChangePassForm(FlaskForm):
    password = PasswordField('New password', validators=[DataRequired()])
    password_confirmed = PasswordField('Confirm new password', validators=[DataRequired()])
    submit = SubmitField('Update password')

class UserMovieReactForm(FlaskForm):
    like = SubmitField('Like')
    dislike = SubmitField('Dislike')

class UserSearchForm(FlaskForm):
    search = SearchField('')

class UserRemoveFriendForm(FlaskForm):
    form_name = HiddenField(default='remove_match_form')
    remove = SubmitField('Remove')

class UserAddFriendForm(FlaskForm):
    form_name = HiddenField(default='add_form')
    add = SubmitField('Add')

class UserSeeMatchesForm(FlaskForm):
    form_name = HiddenField(default='matches_form')
    see_matches = SubmitField('See Matches')

class UserRemoveLikeForm(FlaskForm):
    form_name = HiddenField(default='remove_match_form')
    remove_like = SubmitField('Remove like')