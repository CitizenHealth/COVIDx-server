from flask import request, jsonify
from app import db
from datetime import datetime
import requests
import firebase_admin
from models.survey_response import SurveyResponse
from models.survey_models.health_checkin import HealthCheckin
from models.user import User
from models.survey_models import form_response_models

from . import survey_response
from . import health_checkin
from . import form_submission

@form_submission.route("/submit_form", methods=["POST"])
def form_submission():
    try:
        ### Get user data
        authorization = request.headers.get("Authorization")
        token = authorization.replace('Bearer: ', '', 1)
        fb_id = firebase_admin.auth.verify_id_token(token)['uid']

        user_data = User.query.filter_by(firebase_id=fb_id).first().as_json
        user_id = user_data['user_id']

        ### Choose form model
        request_body = request.get_json()
        form_model = form_response_models[
            request_body['form']
        ]

        ### Convert form results into a form_model object
        form_results = request_body['responses']
        req_data = {
            k: '^_^'.join(v) if type(v) == list 
            else datetime.strptime(v, '%m/%d/%Y') 
            if 'date' in k and v is not None
            else v for k, v in form_results.items()
        }
        req_data['submitted_date'] = datetime.now()
        req_data['user_id'] = user_id

        ### Log the response to the database
        response = form_model(**req_data)
        db.session.add(response)
        db.session.commit()
        return jsonify(message=f"survey responses saved @ => {fb_id}"), 200
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify(message=f"error {str(e)}"), 404
    finally:
        db.session.close()

# getting error, need to check data going through
@survey_response.route("/create_survey_response", methods=["POST"])
def create_survey_response():
    try:
        authorization = request.headers.get("Authorization")
        token = authorization.replace('Bearer: ', '', 1)
        fb_id = firebase_admin.auth.verify_id_token(token)['uid']

        user_data = User.query.filter_by(firebase_id=fb_id).first().as_json
        user_id = user_data['user_id']
        # create new dictionary with parsed data out of the request body
        request_body = request.get_json()
        req_data = {k:(datetime.strptime(v, "%Y-%m-%d") if k.endswith("_date") and v is not None
                    else float(v) if k=="therm_temp" else v if k!="firebase_id" else None) 
                    for k, v in request_body.items()}
        req_data["submitted_date"] = datetime.now()
        req_data["user_id"] = user_id
        # throw this into the survey response model
        survey_response = SurveyResponse(**req_data)
        db.session.add(survey_response)
        db.session.commit()
        return jsonify(message=f"survey responses saved @ => {fb_id}"), 200

    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify(message=f"error {str(e)}"), 404

    finally:
        db.session.close()
