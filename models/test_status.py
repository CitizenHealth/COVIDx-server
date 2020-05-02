from app import db

class TestStatus(db.Model):
    __tablename__ = "test_status"

    test_status_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    survey_id = db.Column(db.Integer(), db.ForeignKey('survey_metadata.survey_id'))
    self_tested = db.Column(db.String(50))
    self_tested_date = db.Column(db.DateTime())
    household_tested = db.Column(db.String(50))
    household_tested_date = db.Column(db.DateTime())

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"test status id => {self.test_status_id}"

