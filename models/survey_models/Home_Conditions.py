
from app import db

class Home_Conditions(db.Model):
    __tablename__ = "home_conditions"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    
    current_symptoms = db.Column(db.String(612))
    fever_best_guess = db.Column(db.String(80))
    how_are_you_feeling = db.Column(db.String(80))
    income = db.Column(db.String(80))
    people_living_with_you = db.Column(db.String(80))
    social_distance_at_home = db.Column(db.String(80))
    temperature = db.Column(db.String(80))
    temperature_scale = db.Column(db.String(80))
    type_of_housing = db.Column(db.String(80))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
