from flask_login import UserMixin
from sqlalchemy import CheckConstraint
from app import db, login_manager


class Location(db.Model):
    """
    figure out where they were at any given time
    """
    user_id = db.Column(db.String(50), primary_key=True, unique=True, nullable=True)
    lat = db.Column(db.Integer())
    lon = db.Column(db.Integer())
    date = db.Column(db.DateTime())

    def __repr__(self):
        return f"role name => {self.name}"