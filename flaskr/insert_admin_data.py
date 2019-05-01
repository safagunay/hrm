import sys
import uuid

from werkzeug.security import generate_password_hash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from models import User

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db = SQLAlchemy(app)
    
    password = "123456"
    if len(sys.argv) > 1:
        password = sys.argv[1]
    admin = User(
        id="adana",
        username='admin', 
        password=generate_password_hash(password)
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin user is added to database.")