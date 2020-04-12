from flask import request, jsonify
from app import db, login_manager
from datetime import datetime
# from firebase_admin import credentials, firestore, initialize_app, auth

from models.user import User, Role


class UserActions:

    def __init__(self, testing=False):
        return

    def get_all():
        """
        return all users
        """
        try:
            query_parameters = request.args
            payload = [i.as_json for i in User.query.all()]

            if payload:
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"

    def register():
        """
        adds the user to db
        """
        try:
            req_data = request.get_json()
            user_id=req_data['user_id']
            display_name = req_data['display_name']
            email = req_data['email']
            date_join = datetime.now()
            img_link = req_data['image']
            # role_id = req_data['role_id']

            user = User(user_id=user_id, 
                        display_name=display_name, 
                        email=email)

            db.session.add(user)
            db.session.commit()      
            return jsonify(payload=user.as_json, ok=True), 200

        except Exception as e:
            db.session.rollback()
            print(f"An Error Occured: {e}")
            return jsonify(payload=None, ok=False), 200

        finally:
            db.session.close()


    def login():
        """
        does this user exist? returns payload
        """
        try:
            query_parameters = request.args
            user_id = query_parameters.get('user_id')

            payload = [i.as_json for i in User.query.filter_by(user_id=user_id)]

            if payload:
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"

    def update():
        """
        update fields
        """
        try:
            query_parameters = request.args
            user_id = query_parameters.get('user_id')

            user = User.query.filter_by(user_id=user_id)
            if user:
                # existing_keys = [k for k, v in query_parameters.items() if v]
                for k, v in query_parameters.items():
                    user[k] = v
                db.session.commit()
                return jsonify(ok=True), 200

            else:
                return jsonify(ok=False), 200

        except Exception as e:
            return f"An Error Occured: {e}"
