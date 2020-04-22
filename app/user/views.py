from flask_login import login_required, login_user, logout_user

from .actions import UserActions
from . import user


@user.route('/create_user', methods=['POST'])
def create_user():
    return UserActions.register()

@user.route('/new_login_user', methods=['PUT'])
def login_user():
    return UserActions.login()
# alternatively, can do the "check if logged in, and if not, register" here

@user.route('/check_token', methods=['GET'])
def check_logged_user():
    return UserActions.check_token()

@user.route('/update_user', methods=['PUT'])
def update_user():
    return UserActions.update()

@user.route('/all_users', methods=['GET'])
def all_users():
    return UserActions.get_all()