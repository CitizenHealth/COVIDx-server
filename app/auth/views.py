from flask_login import login_required, login_user, logout_user

from data_interface import UserActions
from . import auth


@auth.route('/create_user', methods=['POST'])
def create_user():
    return UserActions.register()


@auth.route('/login_user', methods=['GET'])
def login_user():
    return UserActions.login()
