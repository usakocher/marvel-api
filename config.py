import os

from flask_sqlalchemy import SQLAlchemy

# Setting path to the file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'You shall not pass'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    