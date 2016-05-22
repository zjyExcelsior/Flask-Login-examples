from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login' # endpoint
db = SQLAlchemy()

def create_app():
    login_manager.init_app(app)
    db.init_app(app)
    return app

from . import views
from . import models
