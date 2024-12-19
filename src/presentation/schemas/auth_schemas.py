from pydantic import BaseModel


class AuthResponseSchema(BaseModel):
    auth_token: str
    refresh_token: str
