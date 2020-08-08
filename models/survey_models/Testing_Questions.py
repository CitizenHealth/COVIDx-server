
from app import db

class Testing_Questions(db.Model):
    __tablename__ = "testing_questions"

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
    household_date_tested = db.Column(db.String(80))
    household_tested = db.Column(db.String(80))
    how_are_you_feeling = db.Column(db.String(80))
    self_date_tested = db.Column(db.String(80))
    self_tested = db.Column(db.String(80))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
