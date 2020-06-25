from flask import Blueprint

survey_response = Blueprint("survey_response", __name__)
health_checkin = Blueprint("health_checkin", __name__)
from . import views

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
