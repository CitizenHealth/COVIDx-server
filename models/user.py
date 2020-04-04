from typing import Optional, List
from flask_pydantic import validate
from pydantic import BaseModel
import uuid

# app = Flask

class User(BaseModel):
    name: str
    email: str
    role: int
    user_uuid: uuid.UUID


class Devices(BaseModel):
    user_uuid: uuid.UUID
    devices: List[str]