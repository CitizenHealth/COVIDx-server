from app import db

class TripSurveyResponse(db.Model):
    __tablename__ = "tripetto_survey_response"

    response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,  # nullable=True
    )
    user_id = db.Column(db.String(50), db.ForeignKey("users.user_id"))

