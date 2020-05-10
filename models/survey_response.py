from sqlalchemy_utils import create_view
from app import db
from sqlalchemy import CheckConstraint

# having an error - sqlalchemy is trying to merge tables that haven't been created yet
# class SurveyResponse(db.Model):
#     query = db.session.query(
#         SurveyMetadata,
#     ).join(Location).join(MedicalHistory) \
#     .join(Sentiment).join(Symptom) \
#     .join(Temperature).join(TestStatus)

#     view = create_view("survey_response", query, metadata=db.metadata)
#     __table__ = view

#     @property
#     def as_json(self):
#         return {col.name: getattr(self, col.name) for col in self.__table__.columns}



# TODO: split this into a few tables
class SurveyResponse(db.Model):
    __tablename__ = "survey_responses"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.String(50), db.ForeignKey("users.user_id"))
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    self_tested = db.Column(db.String(50))
    self_tested_date = db.Column(db.DateTime())
    household_tested = db.Column(db.String(50))
    household_tested_date = db.Column(db.DateTime())
    therm_temp = db.Column(db.Float())
    temp_guess = db.Column(db.String(50))
    sex = db.Column(db.String(2), CheckConstraint("sex in ('m', 'f')"))
    age = db.Column(db.String(50))
    dry_cough = db.Column(db.Boolean())
    no_smell_taste = db.Column(db.Boolean())
    extreme_fatigue = db.Column(db.Boolean())
    wet_cough = db.Column(db.Boolean())
    dry_cough = db.Column(db.Boolean())
    abdominal_pain = db.Column(db.Boolean())
    diarrhea = db.Column(db.Boolean())
    sore_throat = db.Column(db.Boolean())
    chills = db.Column(db.Boolean())
    nausea_vomiting = db.Column(db.Boolean())
    pressure_chest = db.Column(db.Boolean())
    pink_eye = db.Column(db.Boolean())
    other = db.Column(db.Boolean())
    high_blood_pressure = db.Column(db.Boolean())
    asthma = db.Column(db.Boolean())
    copd_emphysema = db.Column(db.Boolean())
    chronic_kidney_disease = db.Column(db.Boolean())
    liver_disease = db.Column(db.Boolean())
    cancer = db.Column(db.Boolean())
    diabetes = db.Column(db.Boolean())
    cardiovascular_disease = db.Column(db.Boolean())
    hiv_aids = db.Column(db.Boolean())
    bmi_over_40 = db.Column(db.Boolean())
    submitted = db.Column(db.DateTime())
    feeling_well = db.Column(db.String(50))
    sentiment = db.Column(db.String(250))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

