from app import db

class MedicalHistory(db.Model):
    __tablename__ = "medical_history"

    medical_history_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,  # nullable=True
    )
    user_id = db.Column(db.String(50), db.ForeignKey("users.user_id"))
    
