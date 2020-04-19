from flask_login import UserMixin
from sqlalchemy import CheckConstraint
# from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    user table...
    do we assign our own ids? use oauth ids??
    """

    __tablename__ = "users"

    user_id = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(50))
    display_name = db.Column(db.String(50))
    birth = db.Column(db.DateTime())
    zip_code = db.Column(db.String(10))
    # password_hash = db.Column(db.String(128)) check if we still need this with oauth
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_staff = db.Column(db.Boolean, default=False)
    date_join = db.Column(db.DateTime())
    img_link = db.Column(db.String(50))
    sticky_lat = db.Column(db.Float())
    sticky_lon = db.Column(db.Float())

    @property
    def as_json(self):
        return {
            "user_id": self.user_id, 
            "email": self.email, 
            "display_name":self.display_name,
            "birth": self.birth,
            "sex": self.sex,
            "zip_code": self.zip_code,
            "is_staff": self.is_staff,
            "date_join": self.date_join,
            "img_link": self.img_link,
            "sticky_lat": self.sticky_lat,
            "sticky_lon": self.sticky_lon,
        }

    def __repr__(self):
        return f"user email => {self.email}"


class Role(db.Model):
    """
    role table...
    """

    __tablename__="roles"

    role_id = db.Column(db.String(50), primary_key=True, unique=True)
    name = db.Column(db.String(50), index=True)
    description = db.Column(db.String(50), index=True)

    def __repr__(self):
        return f"role name => {self.name}"

