from typing import Coroutine
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from domain.models.user_model import User
from domain.repositories.user_repository import UserRepository


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__()

    async def get_user_by_id(self, user_id: UUID) -> Coroutine[None, None, User]:
        user_found = await self.session.scalar(select(User).where(user_id == User.id))
        return user_found

    async def get_user_by_phone_number(
        self,
        phone_number: str,
    ) -> Coroutine[None, None, User]:
        user_found = await self.session.scalar(
            select(User).where(phone_number == User.phone_number)
        )
        return user_found

    async def create(
        self,
        name: str,
        phone_number: str,
        password: str,
    ) -> Coroutine[None, None, User]:
        user_to_create = User()
