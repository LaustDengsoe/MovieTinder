from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

db = "dbname='site' user='postgres' host='127.0.0.1' password = 'postgres'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'Login.login'
login_manager.login_message_category = 'info'

from MovieTinder.Login.routes import Login
from MovieTinder.Users.routes import Users
app.register_blueprint(Login)
app.register_blueprint(Users)