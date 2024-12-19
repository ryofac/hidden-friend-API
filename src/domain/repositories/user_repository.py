from abc import ABC, abstractmethod
from typing import Coroutine
from uuid import UUID

from domain.models.user_model import User


class UserRepository(ABC):
    @abstractmethod
    async def get_user_by_id(user_id: UUID) -> Coroutine[None, None, User]:
        pass

    @abstractmethod
    async def get_user_by_phone_number(
        phone_number: str,
    ) -> Coroutine[None, None, User]:
        pass

    @abstractmethod
    async def create(
        name: str,
        phone_number: str,
        password: str,
    ) -> Coroutine[None, None, User]:
        pass
