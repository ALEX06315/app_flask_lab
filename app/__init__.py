from flask import Flask
from utils.config import get
my_app = Flask(get("FLASK_APP"))
my_app.debug = get("FLASK_DEBUG", int) or False

from .users import users_blueprint
from .views import main, home
my_app.register_blueprint(users_blueprint)