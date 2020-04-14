from app import db


class SurveyResponse(db.Model):
    __tablename__ = "survey_responses"

    location_id = db.Column(db.String(50), primary_key=True, unique=True, nullable=True)
    user_id = db.Column(db.String(50), db.ForeignKey("users.user_id"))
    self_test_result = db.Column(db.String(50))
    self_test_date = db.Column(db.DateTime())
    household_test_result = db.Column(db.String(50))
    household_test_date = db.Column(db.DateTime())
    thermometer_temp = db.Column(db.Float())
    temp_guess = db.Column(db.String(50))
    has_symptom_dry_cough = db.Column(db.Boolean())
    has_symptom_no_smell_taste = db.Column(db.Boolean())
    has_symptom_extreme_fatigue = db.Column(db.Boolean())
    has_symptom_wet_cough = db.Column(db.Boolean())
    has_symptom_dry_cough = db.Column(db.Boolean())
    has_symptom_abdominal_pain = db.Column(db.Boolean())
    has_symptom_diarrhea = db.Column(db.Boolean())
    has_symptom_sore_throat = db.Column(db.Boolean())
    has_symptom_chills = db.Column(db.Boolean())
    has_symptom_nausea_vomiting = db.Column(db.Boolean())
    has_symptom_pressure_chest = db.Column(db.Boolean())
    has_symptom_pink_eye = db.Column(db.Boolean())
    has_symptom_other = db.Column(db.Boolean())
