from flask_login import login_required, login_user, logout_user

from data_interface import UserActions
from . import auth


@auth.route('/create_user', methods=['POST'])
def create_user():
    return UserActions.register()


@auth.route('/login_user', methods=['GET'])
def read_user():
    return UserActions.login()


@auth.route('/authenticate_user', methods=['GET', 'POST'])
def auth_user():
    return UserActions.login_switch()


# @auth.route("/logout")