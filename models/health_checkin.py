from app import db
from sqlalchemy import CheckConstraint


class HealthCheckin(db.Model):
    __tablename__ = "health_checkin"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    how_are_you_feeling = db.Column(db.Integer())
    current_symptoms = db.Column(db.String(300))
    temperature = db.Column(db.Float())
    self_tested = db.Column(db.String(80))
    self_date_tested = db.Column(db.DateTime())
    household_tested = db.Column(db.String(80))
    household_date_tested = db.Column(db.DateTime())
    medical_conditions = db.Column(db.String(300))
    fever_best_guess = db.Column(db.String(50))
    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

