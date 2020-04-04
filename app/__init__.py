from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config
# from data_interface import User

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You need to be logged in."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    @app.route("/")
    def hello_world():
        return "Hello World"

    # @app.route('/create_user', methods=['POST'])
    # def create_user():
    #     return User.create()

    # @app.route('/read_user', methods=['GET'])
    # def read_user():
    #     return User.read()

    from models import user

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app