# from typing import Optional, List
# # from flask_pydantic import validate
# # from pydantic import BaseModel
# import uuid

# # app = Flask

# class User(BaseModel):
#     name: str
#     email: str
#     role: int
#     user_uuid: uuid.UUID


# class Devices(BaseModel):
#     user_uuid: uuid.UUID
#     devices: List[str]

from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    user table...
    do we assign our own ids? use oauth ids??
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), index=True, unique=True)
    name = db.Column(db.String(50), index=True, unique=True)
    # password_hash = db.Column(db.String(128)) check if we still need this with oauth
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_staff = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"user email => {self.email}"



class Role(db.Model):
    """
    role table...
    """

    __tablename__="roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    description = db.Column(db.String(50), index=True, unique=True)

    def __repr__(self):
        return f"role name => {self.name}"

