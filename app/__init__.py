from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from google.oauth2 import id_token
import os
from config import app_config
import requests


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    if os.getenv("FLASK_CONFIG") == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI"),
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile("config.py")

    db.init_app(app)
    login_manager.init_app(app)

    migrate = Migrate(app, db, compare_type=True)


    @login_manager.request_loader
    @app.before_request
    def firebase_auth(request):
        authorization = request.headers.get("Authorization")
        
        try:
            token = authorization.replace('Bearer: ', '', 1)
            claims = id_token.verify_firebase_token(token, requests.Request())
        
        except:
            raise ValueError("invalid firebase token bro")

        user = await user


    @app.route("/")
    def homepage():
        return "homepage"

    @app.route("/create_data")
    def create_test_user():
        from models.user import User
        payload = {'user_id':'1', 'email':'bob@test.com'}
        user = User(**payload)
        db.session.add(user)
        db.session.commit()
        return "fake user has been created!"


    with app.app_context():
        # from models import user
        
        from .admin import admin as admin_blueprint
        from .user import user as user_blueprint
        from .location import location as location_blueprint
        from .survey_response import survey_response as survey_response_blueprint
        from .auth import auth as auth_blueprint

        app.register_blueprint(admin_blueprint, url_prefix="/admin")
        app.register_blueprint(user_blueprint)
        app.register_blueprint(location_blueprint)
        app.register_blueprint(survey_response_blueprint)
        app.register_blueprint(auth_blueprint)

        db.create_all()

    return app
