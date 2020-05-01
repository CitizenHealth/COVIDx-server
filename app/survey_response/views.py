from flask import request, jsonify
from app import db
from datetime import datetime

from models.survey_response import SurveyResponse

from . import survey_response


@survey_response.route("/create_survey_response", methods=["POST"])
def create_survey_response():
    try:
        req_data = {}
        for k, v in request.get_json().items():
            if v == "null":
                continue
            elif k in _SYMPTOMS:
                req_data[f"has_symptom_{k}"] = v
            elif k in _HISTORIES:
                req_data[f"history_{k}"] = v
            elif k == "therm_temp":
                req_data[k] = float(v)
            elif k.endswith("_date") and v is not None:
                req_data[k] = datetime.strptime(v, "%Y-%m-%d") 
            else:
                req_data[k] = v
        req_data["datetime_submitted"] = datetime.now()

        survey_response = SurveyResponse(**req_data)

        db.session.add(survey_response)
        db.session.commit()
        return jsonify(payload=survey_response.as_json, ok=True), 200

    except Exception as e:
        db.session.rollback()
        print(f"An Error Occured: {e}")
        return jsonify(payload=None, ok=False, error=str(e)), 404

    finally:
        db.session.close()
