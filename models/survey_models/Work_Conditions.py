
from app import db

class Work_Conditions(db.Model):
    __tablename__ = "work_conditions"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    
    close_contact_with_people = db.Column(db.String(80))
    commute_to_work = db.Column(db.String(80))
    current_symptoms = db.Column(db.String(606))
    days_need_to_commute = db.Column(db.String(80))
    do_you_work = db.Column(db.String(80))
    how_are_you_feeling = db.Column(db.String(80))
    industry = db.Column(db.String(2744))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
