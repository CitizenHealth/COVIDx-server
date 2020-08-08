
from app import db

class Medical_History(db.Model):
    __tablename__ = "medical_history"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    
    bmi = db.Column(db.String(80))
    current_symptoms = db.Column(db.String(612))
    do_you_smoke = db.Column(db.String(80))
    fever_best_guess = db.Column(db.String(80))
    have_health_insurance = db.Column(db.String(80))
    how_are_you_feeling = db.Column(db.String(80))
    medical_conditions = db.Column(db.String(376))
    medications = db.Column(db.String(300))
    recent_doctor_visit = db.Column(db.String(80))
    temperature = db.Column(db.String(80))
    temperature_scale = db.Column(db.String(80))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
