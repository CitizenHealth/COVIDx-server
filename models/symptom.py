from app import db

# class Symptom(db.Model):
#     __tablename__ = "symptom"

#     symptom_id = db.Column(
#         db.Integer(),
#         primary_key=True,
#         autoincrement=True,
#         unique=True,
#     )
#     survey_id = db.Column(db.Integer(), db.ForeignKey('survey_metadata.survey_id'))
#     dry_cough = db.Column(db.Boolean())
#     no_smell_taste = db.Column(db.Boolean())
#     extreme_fatigue = db.Column(db.Boolean())
#     wet_cough = db.Column(db.Boolean())
#     dry_cough = db.Column(db.Boolean())
#     abdominal_pain = db.Column(db.Boolean())
#     diarrhea = db.Column(db.Boolean())
#     sore_throat = db.Column(db.Boolean())
#     chills = db.Column(db.Boolean())
#     nausea_vomiting = db.Column(db.Boolean())
#     pressure_chest = db.Column(db.Boolean())
#     pink_eye = db.Column(db.Boolean())
#     other = db.Column(db.Boolean())
#     feeling_well = db.Column(db.String(50))

#     @property
#     def as_json(self):
#         return {col.name: getattr(self, col.name) for col in self.__table__.columns}

#     def __repr__(self):
#         return f"symptom id => {self.symptom_id}"

