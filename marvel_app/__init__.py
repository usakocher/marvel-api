from flask import Flask
from flask.config import Config
from config import Config
from .authentication.routes import auth
from .site.routes import site

# setting the variable for the flask application and providing it with a name
app = Flask(__name__)

app.config.from_object(Config)

# Registering blueprints for routes
app.register_blueprint(site)
app.register_blueprint(auth)