from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from domain.models.constants import Status


class Event(BaseModel):
    uuid: UUID
    name: str
    status: Status
    started_at: datetime
    created_at: datetime
