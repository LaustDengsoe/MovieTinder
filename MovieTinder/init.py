from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

from MovieTinder.Login.routes import Login
app.register_blueprint(Login)