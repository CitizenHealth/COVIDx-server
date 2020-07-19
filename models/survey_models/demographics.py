from app import db
from sqlalchemy import CheckConstraint


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
    temperature_scale = db.Column(db.String(50))
    fever_best_guess = db.Column(db.String(50))
    current_symptoms = db.Column(db.String(300))
    country = db.Column(db.String(80))
    sex = db.Column(db.String(50))
    year_of_birth = db.Column(db.Integer())
    temperature = db.Column(db.Float())
    racial_groups = db.Column(db.String(300))
    how_are_you_feeling = db.Column(db.Integer())
    ethnic_groups = db.Column(db.String(300))
    email = db.Column(db.String(80))
    zip_code = db.Column(db.String(50))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


