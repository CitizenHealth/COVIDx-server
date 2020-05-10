from app import db

class Points(db.Model):
    __tablename__ = "points"

    points_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
    activity = db.Column(db.String(250))
    points = db.Column(db.Integer())
    datetime_submitted = db.Column(db.DateTime())

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"points id => {self.medical_history_id}"

