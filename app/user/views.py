from flask_login import login_required, login_user, logout_user, current_user

from . import user

from flask import request, jsonify
from app import db, login_manager
from datetime import datetime

from models.user import User, Role



@user.route('/create_user', methods=['POST'])
def create_user():
    try:
        req_data = request.get_json()
        payload = User(**req_data)

        db.session.add(payload)
        db.session.commit()
        return jsonify(payload=payload.as_json, ok=True), 200

    except Exception as e:
        db.session.rollback()
        print(f"An Error Occured: {e}")
        return jsonify(payload=None, ok=False), 404

    finally:
        db.session.close()

@user.route('/new_login_user', methods=['PUT'])
def login_user():
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

@user.route('/check_token', methods=['GET'])
def check_logged_user():
    try:
        query_parameters = request.args
        token = query_parameters.get('access_token')

        payload = User.query.filter_by(access_token=token).first()

        if payload:
            # if this token exists, return the user
            return jsonify(payload=payload.as_json, ok=True), 200

        else:
            return jsonify(payload=None, ok=False), 204

    except Exception as e:
        db.session.rollback()
        print(f"An Error Occured: {e}")
        return jsonify(payload=None, ok=False), 404

    finally:
        db.session.close()


@user.route('/update_user', methods=['PUT'])
def update_user():
    try:
        query_parameters = request.args
        user_id = query_parameters.get('user_id')
        request_body = request.get_json()

        payload = User.query.filter_by(user_id=user_id).first()
        if payload:
            for k, v in request_body.items():
                payload[k] = v
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


@user.route('/get_all_users', methods=['GET'])
def get_all_users():
    try:
        query_parameters = request.args
        payload = [i.as_json for i in User.query.all()]

        if payload:
            return jsonify(payload=payload, ok=True), 200

        else:
            return jsonify(payload=None, ok=False), 204

    except Exception as e:
        return f"An Error Occured: {e}"
