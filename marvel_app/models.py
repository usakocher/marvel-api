from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db = SQLAlchemy()

# Creating user table for database
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True, unique = True)
    first_name = db.Column(db.String(35))
    last_name = db.Column(db.String(35))
    username = db.Column(db.String(35), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    token = db.Column(db.String, unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    character = db.relationship('Character', backref = 'owner', lazy = True)

    def __init__(self, first_name, last_name, username, email, password, token = '', id = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self. username = username
        self.email = email
        self.password = self.set_password(password)
        self.token = self.get_token(24)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def get_token(self, length):
        return secrets.token_hex(length)


# Creating character table for database
class Character(db.Model):
    id = db.Column(db.String, primary_key = True, unique = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = True)
    movies = db.Column(db.String, nullable = True)
    events = db.Column(db.String, nullable = True)
    series = db.Column(db.String, nullable = True)
    powers = db.Column(db.String, nullable = True)
    snapped = db.Column(db.Boolean, nullable = True)
    date_modified = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, description, movies, events, series, powers, snapped, user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.description = description
        self.movies = movies
        self.events = events
        self.series = series
        self.powers = powers
        self.snapped = snapped
        self.user_token = user_token

    def set_id(self):
        return str(secrets.token_urlsafe())

# Creating marshaller
class CharacterSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'description', 'movies', 'events', 'series', 'powers', 'snapped']

character_schema = CharacterSchema()
characters_schema = CharacterSchema(many = True)