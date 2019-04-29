# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""

from flask_sqlalchemy import SQLAlchemy
from flaskr.models import User
from flask_login import LoginManager, login_user
from depot.manager import DepotManager


db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "login"
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

DepotManager.configure('default', {
    'depot.storage_path': './files'
})
depot = DepotManager.get()

