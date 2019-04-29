from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=False)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Unicode, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Unicode, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=True)
    last_name = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    _authenticated = False
    @property
    def is_authenticated(self):
        return self._authenticated
    
    @is_authenticated.setter
    def is_authenticated(self, value):
        if value:
            self._authenticated = True
        else: self._authenticated = False
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id():
        return self.id
    



class Candidate(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Unicode, db.ForeignKey('user.id'), nullable=False)
    cv_fileid = db.Column(db.Unicode, unique=True, nullable=False)

if __name__ == '__main__':
    manager.run()



