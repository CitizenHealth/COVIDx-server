# from app import db
# from sqlalchemy import CheckConstraint


# class SurveyResponse(db.Model):
#     __tablename__ = "survey_responses"

#     survey_response_id = db.Column(
#         db.Integer(),
#         primary_key=True,
#         autoincrement=True,
#         unique=True,
#     )
#     user_id = db.Column(db.String(50), db.ForeignKey("users.user_id"))
    # latitude = db.Column(db.Float())
    # longitude = db.Column(db.Float())
    # self_tested = db.Column(db.String(50))
    # self_tested_date = db.Column(db.DateTime())
    # household_tested = db.Column(db.String(50))
    # household_tested_date = db.Column(db.DateTime())
    # therm_temp = db.Column(db.Float())
    # temp_guess = db.Column(db.String(50))
    # sex = db.Column(db.String(2), CheckConstraint("sex in ('m', 'f')"))
    # age = db.Column(db.String(50))
    # has_symptom_dry_cough = db.Column(db.Boolean())
    # has_symptom_no_smell_taste = db.Column(db.Boolean())
    # has_symptom_extreme_fatigue = db.Column(db.Boolean())
    # has_symptom_wet_cough = db.Column(db.Boolean())
    # has_symptom_dry_cough = db.Column(db.Boolean())
    # has_symptom_abdominal_pain = db.Column(db.Boolean())
    # has_symptom_diarrhea = db.Column(db.Boolean())
    # has_symptom_sore_throat = db.Column(db.Boolean())
    # has_symptom_chills = db.Column(db.Boolean())
    # has_symptom_nausea_vomiting = db.Column(db.Boolean())
    # has_symptom_pressure_chest = db.Column(db.Boolean())
    # has_symptom_pink_eye = db.Column(db.Boolean())
    # has_symptom_other = db.Column(db.Boolean())
    # history_high_blood_pressure = db.Column(db.Boolean())
    # history_asthma = db.Column(db.Boolean())
    # history_copd_emphysema = db.Column(db.Boolean())
    # history_chronic_kidney_disease = db.Column(db.Boolean())
    # history_liver_disease = db.Column(db.Boolean())
    # history_cancer = db.Column(db.Boolean())
    # history_diabetes = db.Column(db.Boolean())
    # history_cardiovascular_disease = db.Column(db.Boolean())
    # history_hiv_aids = db.Column(db.Boolean())
    # history_bmi_over_40 = db.Column(db.Boolean())
    # datetime_submitted = db.Column(db.DateTime())
    # feeling_well = db.Column(db.String(50))

    # @property
    # def as_json(self):
    #     return {col.name: getattr(self, col.name) for col in self.__table__.columns}
