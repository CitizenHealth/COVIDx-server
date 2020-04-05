from flask import request, jsonify
from app import db, login_manager
# from firebase_admin import credentials, firestore, initialize_app, auth

from models.user import User


class UserActions:

    def __init__(self, testing=False):
        return

    def register():
        """
        adds the user to db
        """
        try:
            query_parameters = request.args
            id = query_parameters.get('id')
            name = query_parameters.get('name')
            email = query_parameters.get('email')
            # role_id = query_parameters.get('role_id')
            is_staff = query_parameters.get('is_staff')

            user = User(id=id, 
                        name=name, 
                        email=email, 
                        is_staff=is_staff)

            db.session.add(user)
            db.session.commit()
            return jsonify({"ok": True}), 200

        except Exception as e:
            return f"An Error Occured: {e}"


    def login():
        """
        does this user exist? returns a yes/no
        """
        try:
            query_parameters = request.args
            id = query_parameters.get('id')
            name = query_parameters.get('name')
            email = query_parameters.get('email')
            role_id = query_parameters.get('role_id')
            is_staff = query_parameters.get('is_staff')

            if User.query.filter_by(id=id, 
                                    name=name, 
                                    email=email, 
                                    role_id=role_id, 
                                    is_staff=is_staff).all():
                return jsonify({"userExist":True}), 200

            else:
                return jsonify({"userExist":False}), 200

        except Exception as e:
            return f"An Error Occured: {e}"


    # def login_switch():
    #     if login():
    #         return jsonify({"ok": True}), 200
    #         # do something
    #     else: 
    #         register()