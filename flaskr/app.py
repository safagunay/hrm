from flask import Flask
from flask_migrate import Migrate
from flaskr.extensions import db, login_manager
from flaskr.index import bp

#application factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('config.py', silent=False)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    """Register Flask extensions."""
    login_manager.init_app(app)
    db.init_app(app)

def register_blueprints(app):
    app.register_blueprint(bp)