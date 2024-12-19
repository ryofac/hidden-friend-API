from litestar.connection import ASGIConnection
from litestar.di import Provide
from litestar.middleware import (
    AbstractAuthenticationMiddleware,
    AuthenticationResult,
)

from application.providers.token_provider import TokenProvider
from domain.repositories.user_repository import UserRepository
from infra.providers.josetoken_provider import JoseTokenProvider
from infra.sqlalchemy.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from presentation.exceptions.auth_exceptions import (
    UnauthorizedCredentialsException,
)


class JWTAuthMiddleware(AbstractAuthenticationMiddleware):
    def __init__(
        self,
        app,
        exclude=None,
        exclude_from_auth_key="exclude_from_auth",
        exclude_http_methods=None,
        scopes=None,
    ):
        self.user_repository: UserRepository = Provide(SQLAlchemyUserRepository)
        self.token_provider: TokenProvider = Provide(JoseTokenProvider)
        super().__init__(
            app, exclude, exclude_from_auth_key, exclude_http_methods, scopes
        )

    async def authenticate_request(
        self,
        connection: ASGIConnection,
    ) -> AuthenticationResult:
        auth = connection.headers.get("Authorization")
        if not auth:
            raise UnauthorizedCredentialsException()

        _, auth_token = auth.split(" ")[:3]

        user_info = self.token_provider.decode(auth_token)
        user_phone = user_info["sub"]
        user = await self.user_repository.get_user_by_phone_number(user_phone)

        return AuthenticationResult(user, auth_token)
