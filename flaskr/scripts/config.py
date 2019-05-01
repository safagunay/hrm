import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY='dev'
SQLALCHEMY_DATABASE_URI="postgresql://postgresondocker:postgresondocker@localhost:5432/postgresondocker"
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False