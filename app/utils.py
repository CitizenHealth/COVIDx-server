from models.user import Role
from app import db

# create roles if they don't exist
def check_staff_role():
    staff_exist = db.session.query(Role.name).filter_by(name="staff").scalar() is not None
    
    if not staff_exist:
        payload = {'user_id':'0', 'name':'staff'}
        role = Role(**payload)
        db.session.add()
        db.session.commit()

        return "staff role has been created!"