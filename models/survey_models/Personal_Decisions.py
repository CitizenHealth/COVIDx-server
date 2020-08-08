
from app import db

class Personal_Decisions(db.Model):
    __tablename__ = "personal_decisions"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    
    current_symptoms = db.Column(db.String(606))
    diets = db.Column(db.String(346))
    exercise_location = db.Column(db.String(80))
    exercises = db.Column(db.String(396))
    food_avoiding = db.Column(db.String(300))
    have_you_left_house = db.Column(db.String(80))
    hours_of_sleep = db.Column(db.String(80))
    hours_per_week_exercise = db.Column(db.String(80))
    how_are_you_feeling = db.Column(db.String(80))
    how_do_you_feel_leaving_house = db.Column(db.String(80))
    protective_measures_enter_home = db.Column(db.String(300))
    protective_measures_left_home = db.Column(db.String(300))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
