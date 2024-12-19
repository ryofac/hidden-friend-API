import token
from dataclasses import dataclass

from application.providers.hash_provider import HashProvider
from domain.models.user_model import User
from domain.repositories import UserRepository
from presentation.exceptions.user_exceptions import (
    CredentialsException,
)


@dataclass
class LoginRequest:
    user_phone_number: str
    user_password: str


@dataclass
class LoginResponse:
    user: User
    token: str


class LoginUserUsecase:
    def __init__(
        self,
        user_repository: UserRepository,
        hash_provider: HashProvider,
    ):
        self.user_repository = user_repository
        self.hash_provider = hash_provider

    async def execute(self, login_data: LoginRequest) -> LoginResponse:
        user_found: User = await self.user_repository.get_user_by_phone_number(
            login_data.user_phone_number,
        )

        if not user_found:
            raise CredentialsException()

        valid_login = self.hash_provider.verify(
            user_found.password, login_data.user_password
        )

        if not valid_login:
            raise CredentialsException()

        return {"user": user_found, "token": token}
