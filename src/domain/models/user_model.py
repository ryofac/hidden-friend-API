import datetime
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    phone_number: str
    name: str
    password: str
    joined_at: datetime
    edited_at: datetime
