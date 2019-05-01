import os
basedir = os.path.abspath(os.path.dirname(__file__))

# DEBUG = False
# TESTING = False
# CSRF_ENABLED = True
SECRET_KEY='665a23a8-4c8e-40c4-9fa9-1dcfc5a12de0'
SQLALCHEMY_DATABASE_URI="postgresql://postgresondocker:postgresondocker@localhost:5432/postgresondocker"
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False

# class Config(object):
#     # DEBUG = False
#     # TESTING = False
#     # CSRF_ENABLED = True
#     SECRET_KEY='dev'
#     DATABASE="postgresql://postgresondocker:postgresondocker@localhost:5432/flaskdeneme"
#     SQLALCHEMY_DATABASE_URI="postgresql://postgresondocker:postgresondocker@localhost:5432/flaskdeneme"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# class ProductionConfig(Config):
#     DEBUG = False


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class TestingConfig(Config):
#     TESTING = True