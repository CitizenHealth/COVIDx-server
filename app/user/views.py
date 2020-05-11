# from flask_login import login_required, login_user, logout_user, current_user

from . import user

from flask import request, jsonify
from app import db

from models.user import User
# from models.covid_status import CovidStatus

from firebase_admin import auth

# @user.route('/create_user', methods=['POST'])
# def create_user():
#     try:
#         req_data = request.get_json()
#         payload = User(**req_data)

#         db.session.add(payload)
#         db.session.commit()
#         return jsonify(payload=payload.as_json, ok=True), 200

#     except Exception as e:
#         db.session.rollback()
#         print(f"An Error Occured: {e}")
#         return jsonify(payload=None, ok=False), 404

#     finally:
#         db.session.close()

# @user.route('/new_login_user', methods=['PUT'])
# def login_user():
#     try:
#         user_id = request.args.get('user_id')
#         token = request.get_json()['access_token']

#         payload = User.query.filter_by(user_id=user_id).first()

#         if payload:
#             # add the new web token to db
#             payload.access_token = token
#             db.session.commit()
#             return jsonify(payload=payload.as_json, ok=True), 200

#         else:
#             return jsonify(payload=None, ok=False), 204

#     except Exception as e:
#         db.session.rollback()
#         print(f"An Error Occured: {e}")
#         return jsonify(payload=None, ok=False), 404

#     finally:
#         db.session.close()

# @user.route('/check_token', methods=['GET']) # TODO: I DON'T THINK WE NEED THIS ANYMORE
# def check_logged_user():
#     try:
#         query_parameters = request.args
#         token = query_parameters.get('access_token')

#         payload = User.query.filter_by(access_token=token).first()

#         if payload:
#             # if this token exists, return the user
#             return jsonify(payload=payload.as_json, ok=True), 200

#         else:
#             return jsonify(payload=None, ok=False), 204

#     except Exception as e:
#         db.session.rollback()
#         print(f"An Error Occured: {e}")
#         return jsonify(payload=None, ok=False), 404

#     finally:
#         db.session.close()

# @user.route('/login_user', methods=['POST']) # TODO: FILL IN THE FB AUTH STUFFS
# def login_user():
#     try:
#         request_body = request.get_json()
#         # fb_id = request.headers.get('Authorization')
#         fb_id = request_body['firebase_id']
#         payload = User.query.filter_by(firebase_id=fb_id).first()

#         if payload:
#             return jsonify(message=f"user exists @ => {fb_id}"), 200
#         else:
#             auth_data = get_user(fb_id)
#             # get data from google thru fb_id
#             # get this user's info here as dict
#             auth.auth_payload = User(**auth_data)
#             db.session.add(auth_payload)
#             db.session.commit()
#             return jsonify(message=f"user created @ => {fb_id}"), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify(message=f"error {str(e)}"), 404

#     finally:
#         db.session.close()


@user.route('/update_user', methods=['PUT'])
def update_user():
    try:
        request_body = request.get_json()
        fb_id = request_body.get('firebase_id')
        payload = User.query.filter_by(firebase_id=fb_id).first()

        if payload:
            for k, v in request_body.items():
                payload[k] = v
            db.session.commit()
            return jsonify(message=f"user updated @ => {fb_id}"), 200

        else:
            return jsonify(message=f"user not found @ => {fb_id}"), 204

    except Exception as e:
        db.session.rollback()
        return jsonify(message=f"error {str(e)}"), 404

    finally:
        db.session.close()


# @user.route('/get_all_users', methods=['GET'])
# def get_all_users():
#     try:
#         # query_parameters = request.args
#         payload = [i.as_json for i in User.query.all()]

#         if payload:
#             return jsonify(payload=payload, message="user found!"), 200

#         else:
#             return jsonify(payload=None, message="user not found :("), 204

#     except Exception as e:
#         return jsonify(message=f"error {str(e)}"), 404

# generic "create covid status function, don't know where this will come from"
@user.route('/create_covid_status', methods=['PUT'])
def create_covid_status():
    try:
        request_body = request.get_json()
        fb_id = request_body.get('firebase_id')
        # get user id using fb id from user table
        user_data = User.query.filter_by(firebase_id=fb_id).first()
        user_id = user_data['user_id']
        # replace firebase id for user id 
        req_sending = {k:v for k, v in request_body if k!='firebase_id'}
        req_sending['user_id'] = user_id
        # send this info over to db
        payload = CovidStatus(**req_sending)
        db.session.add(payload)
        db.session.commit()
        return jsonify(message=f"covid status updated @ {user_id}")

    except Exception as e:
        db.session.rollback()
        return jsonify(message=f"error {str(e)}"), 404

    finally:
        db.session.close()
