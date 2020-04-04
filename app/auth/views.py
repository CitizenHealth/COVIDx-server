from data_interface import User
from . import auth


@auth.route('/create_user', methods=['POST'])
def create_user():
    return User.create()


@auth.route('/read_user', methods=['GET'])
def read_user():
    return User.read()

# @auth.route("/logout")