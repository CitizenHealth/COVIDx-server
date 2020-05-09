from app import db

class CovidStatus(db.Model):
    __tablename__ = "covid_status"

    covid_status_id = db.Column(
        db.Integer(), 
        primary_key=True, 
        unique=True, 
        nullable=False,
        autoincrement=True
    )
    user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
    covid_status = db.Column(db.String(50))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"covid id => {self.covid_status_id}"
