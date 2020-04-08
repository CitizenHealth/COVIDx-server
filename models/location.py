from typing import Optional, List
from flask_pydantic import validate
from pydantic import BaseModel
import uuid

# app = Flask

class Location(BaseModel):
    user_uuid: uuid.UUID
    date_coords: dict = None