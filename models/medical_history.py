from app import db

# class MedicalHistory(db.Model):
#     __tablename__ = "medical_history"

#     medical_history_id = db.Column(
#         db.Integer(),
#         primary_key=True,
#         autoincrement=True,
#         unique=True,
#     )
#     survey_id = db.Column(db.Integer(), db.ForeignKey('survey_metadata.survey_id'))
#     high_blood_pressure = db.Column(db.Boolean())
#     asthma = db.Column(db.Boolean())
#     copd_emphysema = db.Column(db.Boolean())
#     chronic_kidney_disease = db.Column(db.Boolean())
#     liver_disease = db.Column(db.Boolean())
#     cancer = db.Column(db.Boolean())
#     diabetes = db.Column(db.Boolean())
#     cardiovascular_disease = db.Column(db.Boolean())
#     hiv_aids = db.Column(db.Boolean())
#     bmi_over_40 = db.Column(db.Boolean())

#     @property
#     def as_json(self):
#         return {col.name: getattr(self, col.name) for col in self.__table__.columns}

#     def __repr__(self):
#         return f"medical history id => {self.medical_history_id}"

