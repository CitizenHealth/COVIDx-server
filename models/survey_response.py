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
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    submitted_date = db.Column(db.DateTime())
    abdominal_pain = db.Column(db.Boolean())
    age = db.Column(db.Integer())
    asthma = db.Column(db.Boolean())
    bmi_over_40 = db.Column(db.Boolean())
    cancer = db.Column(db.Boolean())
    cardiovascular_disease = db.Column(db.Boolean())
    chest_pain = db.Column(db.Boolean())
    chills = db.Column(db.Boolean())
    chronic_kidney_disease = db.Column(db.Boolean())
    copd_emphysema = db.Column(db.Boolean())
    diabetes = db.Column(db.Boolean())
    diarrhea = db.Column(db.Boolean())
    dry_cough = db.Column(db.Boolean())
    extreme_fatigue = db.Column(db.Boolean())
    headache = db.Column(db.Boolean())
    high_blood_pressure = db.Column(db.Boolean())
    hiv_aids = db.Column(db.Boolean())
    household_tested = db.Column(db.String(50))
    household_tested_date = db.Column(db.DateTime())
    liver_disease = db.Column(db.Boolean())
    loss_of_smell = db.Column(db.Boolean())
    loss_of_taste = db.Column(db.Boolean())
    nausea = db.Column(db.Boolean())
    other = db.Column(db.Boolean())
    rash_on_feet = db.Column(db.Boolean())
    self_tested = db.Column(db.String(50))
    self_tested_date = db.Column(db.DateTime())
    sex = db.Column(db.String(2), CheckConstraint("sex in ('m', 'f')"))
    sore_throat = db.Column(db.Boolean())
    temp_guess = db.Column(db.String(50))
    therm_temp = db.Column(db.Float())
    tightness_chest = db.Column(db.Boolean())
    vomiting = db.Column(db.Boolean())
    wet_cough = db.Column(db.Boolean())

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

