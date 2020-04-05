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

    id = db.Column(db.String(50), primary_key=True, unique=True)
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birth = db.Column(db.Date)
    sex = db.Column(db.String(6), CheckConstraint("sex in ('male', 'female')"))
    zip_code = db.Column(db.String(10))
    # password_hash = db.Column(db.String(128)) check if we still need this with oauth
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_staff = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f"user email => {self.email}"


class Role(db.Model):
    """
    role table...
    """

    __tablename__="roles"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), index=True)
    description = db.Column(db.String(50), index=True)

    def __repr__(self):
        return f"role name => {self.name}"

