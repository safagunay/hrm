# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user
from depot.manager import DepotManager
#from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "Admin.login"

DepotManager.configure('default', {
    'depot.storage_path': './files'
})
depot = DepotManager.get()

#csrf = CSRFProtect()

