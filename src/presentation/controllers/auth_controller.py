from litestar import Controller, post

from application.usecases.login_user_usecase import LoginUserUsecase
from presentation.schemas.auth_schemas import AuthResponseSchema
from presentation.schemas.user_schemas import UserLoginSchema


class AuthController(Controller):
    dependencies = {}
    
    @post("/login", dependencies=)
    async def login(self, data: UserLoginSchema) -> AuthResponseSchema:
        usecase = LoginUserUsecase(repository, hash_provider)

        return AuthResponseSchema(auth_token="", refresh_token="")

    @post("/register")
    async def register(self, data) -> None:
        return {}
