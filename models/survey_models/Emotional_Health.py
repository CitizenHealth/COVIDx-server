
from app import db

class Emotional_Health(db.Model):
    __tablename__ = "emotional_health"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    
    anxiety_level = db.Column(db.String(80))
    current_symptoms = db.Column(db.String(612))
    depression_level = db.Column(db.String(80))
    events_worries = db.Column(db.String(422))
    how_are_you_feeling = db.Column(db.String(80))
    mental_illnesses = db.Column(db.String(300))
    stress_reducing_methods = db.Column(db.String(300))
    talked_to_someone = db.Column(db.String(80))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
