from flask import request, jsonify
from app import db
from datetime import datetime

from models.survey_response import SurveyResponse
from models.user import User

from . import survey_response


@survey_response.route("/create_survey_response", methods=["POST"])
def create_survey_response():
    try:
        request_body = request.get_json()
        fb_id = request_body.get('firebase_id')
        # use fb id to get user id, which we'll then slot in place of the fb id in the request body
        user_data = User.query.filter_by(firebase_id=fb_id).first()
        user_id = user_data['user_id']
        # create new dictionary with parsed data out of the request body
        req_data = {k:datetime.strptime(v, "%Y-%m-%d") if k.endswith("_date") 
                    else k:float(v) if k=="therm_temp" else k:v if k!="firebase_id" 
                    for k, v in request_body.items()}
        # req_data = {}
        # for k, v in request_body.items():
        #     if v == "null":
        #         continue
        #     # elif k in _SYMPTOMS:
        #     #     req_data[k] = v
        #     # elif k in _HISTORIES:
        #     #     req_data[k] = v
        #     elif k == "therm_temp":
        #         req_data[k] = float(v)
        #     elif k.endswith("_date") and v is not None:
        #         req_data[k] = datetime.strptime(v, "%Y-%m-%d") 
        #     else:
        #         req_data[k] = v
        req_data["datetime_submitted"] = datetime.now()
        # throw this into the survey response model
        survey_response = SurveyResponse(**req_data)
        db.session.add(survey_response)
        db.session.commit()
        return jsonify(message=f"survey responses saved @ => {fb_id}"), 200

    except Exception as e:
        db.session.rollback()
        return jsonify(message=f"error {str(e)}"), 404

    finally:
        db.session.close()
