from app import db

# class Temperature(db.Model):
#     __tablename__ = "temperature"

#     temperature_id = db.Column(
#         db.Integer(),
#         primary_key=True,
#         autoincrement=True,
#         unique=True,
#     )
#     survey_id = db.Column(db.Integer(), db.ForeignKey('survey_metadata.survey_id'))
#     therm_temp = db.Column(db.Float())
#     temp_guess = db.Column(db.String(50))

#     @property
#     def as_json(self):
#         return {col.name: getattr(self, col.name) for col in self.__table__.columns}

#     def __repr__(self):
#         return f"temperature id => {self.temperature_id}"

