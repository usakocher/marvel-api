import os

from flask_sqlalchemy import SQLAlchemy

# Setting path to the file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'You shall not pass'
    DATABASE_URL = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    