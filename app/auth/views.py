from flask_login import login_required, login_user, logout_user

from data_interface import UserActions
from . import auth


@auth.route('/create_user', methods=['POST'])
def create_user():
    return UserActions.register()

@auth.route('/login_user', methods=['GET'])
def login_user():
    return UserActions.login()

@auth.route('/update_user', methods=['PUT'])
def update_user():
    return UserActions.update()

@auth.route('/all_users', methods=['GET'])
def all_users():
    return UserActions.get_all()