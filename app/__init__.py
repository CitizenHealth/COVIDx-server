from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_migrate import Migrate
# from google.oauth2 import id_token
import os
from config import app_config
import requests
# from firebase_admin import auth, credentials
import firebase_admin
from flask import request

db = SQLAlchemy()
firebase_admin.initialize_app()
# login_manager = LoginManager()


def create_app(config_name):
    if os.getenv("FLASK_CONFIG")=="production":
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

    migrate = Migrate(app, db, compare_type=True)
    

    # @login_manager.request_loader
    @app.before_request
    def firebase_auth():
        from models.user import User
        authorization = request.headers.get("Authorization")
        if "Authorization" not in request.headers:
            return 

        token = authorization.replace('Bearer: ', '', 1)
        decoded = firebase_admin.auth.verify_id_token(token)
        fb_id = decoded['uid']
        # find this in the user model. if it exists, as is. if not, create account
        user = User.query.filter_by(firebase_id=fb_id).first()
        print(user)
        print(f"user found @ => {fb_id}")
        # create account
        if not user:
            # auth_data = firebase_admin.auth.get_user(fb_id)
            # print(auth_data.__dict__)
            payload = User(firebase_id=fb_id)
            # payload = User(**auth_data)
            db.session.add(payload)
            db.session.commit()
            print(f"user created @ => {fb_id}")


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
        from .admin import admin as admin_blueprint
        from .user import user as user_blueprint
        from .location import location as location_blueprint
        from .survey_response import survey_response as survey_response_blueprint
        from .auth import auth as auth_blueprint
        from .survey_response import health_checkin as health_checkin_blueprint
        from .survey_response import form_submission as form_submission_blueprint

        app.register_blueprint(admin_blueprint, url_prefix="/admin")
        app.register_blueprint(user_blueprint)
        app.register_blueprint(location_blueprint)
        app.register_blueprint(survey_response_blueprint)
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(health_checkin_blueprint, url_prefix="/health_checkin")
        app.register_blueprint(form_submission_blueprint)

        # check_staff_role()

        db.create_all()

    return app
