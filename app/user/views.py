from flask_login import login_required, login_user, logout_user

from .actions import UserActions
from . import user


@user.route('/create_user', methods=['POST'])
def create_user():
    return UserActions.register()

@user.route('/login_user', methods=['GET'])
def login_user():
    return UserActions.login()

@user.route('/update_user', methods=['PUT'])
def update_user():
    return UserActions.update()

@user.route('/all_users', methods=['GET'])
def all_users():
    return UserActions.get_all()