from dataclasses import dataclass

from application.providers.hash_provider import HashProvider
from domain.models.user_model import User
from domain.repositories import UserRepository
from presentation.exceptions.user_exceptions import PasswordsDoesNotMatchException


@dataclass
class RegisterRequest:
    phone_number: str
    name: str
    password: str
    confirm_password: str


@dataclass
class RegisterResponse:
    user_created: User


class RegisterUsecase:
    def __init__(self, user_repository: UserRepository, hash_provider: HashProvider):
        self.user_repository = user_repository
        self.hash_provider = hash_provider

    async def execute(self, register_data: RegisterRequest) -> User:
        if register_data.password != register_data.password:
            raise PasswordsDoesNotMatchException()

        user_created = await self.user_repository.create(
            name=register_data.name,
            password=self.hash_provider.hash(register_data.password),
            phone_number=register_data.phone_number,
        )

        return user_created
