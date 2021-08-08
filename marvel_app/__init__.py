from marvel_app.helpers import JSONEncoder
from flask import Flask
from flask.config import Config
from config import Config
from .authentication.routes import auth
from .site.routes import site
from .api.routes import api
from .models import db, User, Character, login_manager, ma
from flask_migrate import Migrate
from flask_cors import CORS

# setting the variable for the flask application and providing it with a name
app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'
migrate = Migrate(app, db)
ma.init_app(app)

# Registering blueprints for routes
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
CORS(app)