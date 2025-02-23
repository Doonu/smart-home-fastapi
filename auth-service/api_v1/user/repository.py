from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.user import User


@dataclass
class UserRepository:
    db_session: AsyncSession

    async def create_user(self, email: str, password: str) -> User:
        user = User(email=email, password=password)
        self.db_session.add(user)
        await self.db_session.commit()
        return user

    async def get_user(self, user_id: int) -> User:
        query = select(User).where(User.id == user_id)

        user = await self.db_session.execute(query)
        return user.scalar()
