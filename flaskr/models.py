#from flaskr.migrate import User, Candidate
from os import path
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flaskr.extensions import depot

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Unicode, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

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
    
    def get_id(self):
        try:
            return "adana"
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
    
class Candidate(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cv_fileid = db.Column(db.Unicode, unique=False, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def cv_fileurl(self):
        return "depot/default/" + self.cv_fileid

    @property
    def table_filename(self):
        file_name = depot.get(self.cv_fileid).filename
        name, ext = path.splitext(file_name)
        if len(name) > 15:
            name = name[:15]
        return name + ext;
