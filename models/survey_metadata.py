from app import db

class SurveyMetadata(db.Model):
    __tablename__ = "survey_metadata"

    survey_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    user_id = db.Column(db.String(50), db.ForeignKey("users.user_id"))
    datetime_submitted = db.Column(db.DateTime())

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"survey metadata id => {self.survey_metadata_id}"

