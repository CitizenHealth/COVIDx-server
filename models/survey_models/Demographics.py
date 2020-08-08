
from app import db

class Demographics(db.Model):
    __tablename__ = "demographics"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    
    country = db.Column(db.String(80))
    current_symptoms = db.Column(db.String(612))
    email = db.Column(db.String(80))
    ethnicity = db.Column(db.String(496))
    fever_best_guess = db.Column(db.String(80))
    how_are_you_feeling = db.Column(db.String(80))
    race = db.Column(db.String(346))
    sex = db.Column(db.String(80))
    temperature = db.Column(db.String(80))
    temperature_scale = db.Column(db.String(80))
    year_of_birth = db.Column(db.String(80))
    zip_code = db.Column(db.String(80))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
