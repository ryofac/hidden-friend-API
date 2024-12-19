from litestar import Controller, post

from presentation.schemas.auth_schemas import AuthResponseSchema
from presentation.schemas.user_schemas import UserLoginSchema


class AuthController(Controller):
    @post("/login")
    async def login(self, data: UserLoginSchema) -> AuthResponseSchema:
        return AuthResponseSchema(auth_token="", refresh_token="")

    @post("/register")
    async def register(self, data) -> None:
        return {}
