from flask import request, jsonify
from app import db
from datetime import datetime

# from firebase_admin import credentials, firestore, initialize_app, auth

from models.survey_response import SurveyResponse

_SYMPTOMS = [
    "dry_cough",
    "no_smell_taste",
    "extreme_fatigue",
    "wet_cough",
    "dry_cough",
    "abdominal_pain",
    "diarrhea",
    "sore_throat",
    "chills",
    "nausea_vomiting",
    "pressure_chest",
    "pink_eye",
    "other",
]

_HISTORIES = [
    "high_blood_pressure",
    "asthma",
    "copd_emphysema",
    "chronic_kidney_disease",
    "liver_disease",
    "cancer",
    "diabetes",
    "cardiovascular_disease",
    "hiv_aids",
    "bmi_over_40",
]


class SurveyResponseActions:
    def __init__(self, testing=False):
        return

    def create():
        """
        stores users survey response in db
        """
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
            return jsonify(payload=None, ok=False), 200

        finally:
            db.session.close()
