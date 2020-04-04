from flask import Flask
from firebase_admin import credentials, firestore, initialize_app, auth
import os

from crud import User

app = Flask(__name__)

# @app.route('/auth', methods=['POST'])
# def user_auth():
    # """
    # authenticate(): Check if username and password match
    # return True or False
    # """

@app.route('/create_user', methods=['POST'])
def create_user():
    return User.create()


@app.route('/read_user', methods=['GET'])
def read_user():
    return User.read()


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)