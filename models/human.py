from app import db

class Human(db.Model):
    __tablename__ = "human"

    user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))
    human_token = db.Column(db.String(250), primary_key=True, unique=True)

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"human token is => {self.human_token}"