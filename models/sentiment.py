from app import db

class Sentiment(db.Model):
    __tablename__ = "sentiment"

    sentiment_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    survey_id = db.Column(db.Integer(), db.ForeignKey('survey_metadata.survey_id'))
    sentiment = db.Column(db.String(250))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"sentiment id => {self.sentiment_id}"

