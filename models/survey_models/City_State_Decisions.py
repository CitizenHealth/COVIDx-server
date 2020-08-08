
from app import db

class City_State_Decisions(db.Model):
    __tablename__ = "city_state_decisions"

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
    governor_orders_rating = db.Column(db.String(80))
    how_are_you_feeling = db.Column(db.String(80))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
