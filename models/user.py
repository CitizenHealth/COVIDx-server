from flask_login import UserMixin
from sqlalchemy import CheckConstraint

from app import db


class User(UserMixin, db.Model):
    """
    user table...
    do we assign our own ids? use fb ids??
    """

    __tablename__ = "users"

    user_id = db.Column(
        db.Integer(), 
        primary_key=True, 
        unique=True, 
        nullable=False,
        autoincrement=True,
    )
    firebase_id = db.Column(db.String(50), unique=True, nullable=False)
    birth = db.Column(db.DateTime())
    sex = db.Column(db.String(2), CheckConstraint("sex in ('m', 'f')"))
    date_birth = db.Column(db.DateTime())
    # role = db.Column(db.Boolean, default=False)
    # role_id = db.Column(db.Integer(), db.ForeignKey("roles.role_id"))
    # date_join = db.Column(db.DateTime())

    @property
    def as_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f"welcome to covidx => {self.user_id}"


# class Role(db.Model):
#     """
#     role table...
#     """

#     __tablename__="roles"

#     role_id = db.Column(
#         db.Integer(), 
#         primary_key=True, 
#         unique=True, 
#         nullable=False,
#     )
#     name = db.Column(db.String(50), index=True)
#     description = db.Column(db.String(50), index=True)

#     @property
#     def as_json(self):
#         return {col.name: getattr(self, col.name) for col in self.__table__.columns}

#     def __repr__(self):
#         return f"role id => {self.role_id}"

