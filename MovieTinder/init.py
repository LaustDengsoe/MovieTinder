from flask import Flask

app = Flask(__name__)

from MovieTinder.Login.routes import Login
app.register_blueprint(Login)