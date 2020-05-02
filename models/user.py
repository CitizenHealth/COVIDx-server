from flask_login import UserMixin
from sqlalchemy import CheckConstraint

from app import db, login_manager


class Users(UserMixin, db.Model):
    """
    user table...
    do we assign our own ids? use fb ids??
    """

    __tablename__ = "users"

    user_id = db.Column(
        db.String(50), 
        primary_key=True, 
        unique=True, 
        nullable=False,
        autoincrement=True,
    )
    firebase_id = db.Column(db.String(50), unique=True, nullable=False)
    birth = db.Column(db.DateTime())
    sex = db.Column(db.String(2), CheckConstraint("sex in ('m', 'f')"))
    date_birth = db.Column(db.DateTime())
    is_staff = db.Column(db.Boolean, default=False)
    date_join = db.Column(db.DateTime())
    img_link = db.Column(db.String(250))

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"welcome to covidx => {self.display_name}"


class Role(db.Model):
    """
    role table...
    """

    __tablename__="roles"

    role_id = db.Column(db.String(50), primary_key=True, unique=True)
    name = db.Column(db.String(50), index=True)
    description = db.Column(db.String(50), index=True)

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"role id => {self.role_id}"

