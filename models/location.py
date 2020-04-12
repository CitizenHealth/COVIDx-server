from flask_login import UserMixin
from sqlalchemy import CheckConstraint
from app import db, login_manager


class Location(db.Model):
    """
    figure out where they were at any given time
    """
    __tablename__ = "location"

    location_id = db.Column(db.String(50), primary_key=True, unique=True, nullable=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.user_id'))
    lat = db.Column(db.Integer())
    lon = db.Column(db.Integer())
    date = db.Column(db.DateTime())

    @property
    def as_json(self):
        return {
            "location_id": self.location_id, 
            "user_id": self.user_id, 
            "lat":self.lat,
            "lon": self.lon,
            "date": self.date,
        }

    def __repr__(self):
        return f"role name => {self.name}"