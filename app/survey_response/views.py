from flask import request, jsonify
from app import db
from datetime import datetime

from models.user import User

from . import survey_response


@survey_response.route("/create_survey_response", methods=["POST"])
def create_survey_response():
    try:
        request_body = request.get_json()
        fb_id = request_body.get('firebase_id')
        user_data = User.query.filter_by(firebase_id=fb_id).first()
        user_id = user_data['user_id']
        # create new dictionary with parsed data out of the request body
        req_data = {k:(datetime.strptime(v, "%Y-%m-%d") if k.endswith("_date") 
                    else float(v) if k=="therm_temp" else v if k!="firebase_id" else None) 
                    for k, v in request_body.items()}
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