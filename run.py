# from flask import Flask
# from firebase_admin import credentials, firestore, initialize_app, auth
import os

# from data_interface import User
from app import create_app

# app = Flask(__name__)

config_name = os.getenv("FLASK_CONFIG")
app = create_app(config_name)

# @app.route('/create_user', methods=['POST'])
# def create_user():
#     return User.create()


# @app.route('/read_user', methods=['GET'])
# def read_user():
#     return User.read()


# port = int(os.environ.get('PORT', 8080))
# if __name__ == '__main__':
#     app.run(threaded=True, host='0.0.0.0', port=port)

if __name__ == "__main__":
    app.run()