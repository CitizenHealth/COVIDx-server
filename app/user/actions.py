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
                return jsonify(payload=None, ok=False), 204

        except Exception as e:
            return f"An Error Occured: {e}"

    def register():
        """
        adds the user to db
        """
        try:
            req_data = request.get_json()
            user = User(**req_data)

            db.session.add(user)
            db.session.commit()
            return jsonify(payload=user.as_json, ok=True), 200

        except Exception as e:
            db.session.rollback()
            print(f"An Error Occured: {e}")
            return jsonify(payload=None, ok=False), 404

        finally:
            db.session.close()


    def login():
        """
        does this user exist? if so, create a token for them, and return the new values
        """
        try:
            user_id = request.args.get('user_id')
            token = request.get_json()['access_token']

            payload = User.query.filter_by(user_id=user_id).first()

            if payload:
                # add the new web token to db
                payload.access_token = token
                db.session.commit()
                return jsonify(payload=payload.as_json, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 204

        except Exception as e:
            db.session.rollback()
            print(f"An Error Occured: {e}")
            return jsonify(payload=None, ok=False), 404

        finally:
            db.session.close()

    def check_token():
        """
        use this function to check whether or not this token exists - return user data
        """
        try:
            query_parameters = request.args
            token = query_parameters.get('access_token')

            payload = [i.as_json for i in User.query.filter_by(access_token=token)]

            if payload:
                # if this token exists, return the user
                return jsonify(payload=payload, ok=True), 200

            else:
                return jsonify(payload=None, ok=False), 204

        except Exception as e:
            db.session.rollback()
            print(f"An Error Occured: {e}")
            return jsonify(payload=None, ok=False), 404

        finally:
            db.session.close()


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
                return jsonify(ok=False), 204

        except Exception as e:
            return f"An Error Occured: {e}"
