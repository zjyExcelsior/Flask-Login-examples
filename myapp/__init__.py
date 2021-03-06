# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'  # endpoint
db = SQLAlchemy()
from .views.main import main
from .views.auth import auth


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    login_manager.init_app(app)
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app
