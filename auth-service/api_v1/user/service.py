from dataclasses import dataclass

from api_v1.user import UserLoginSchema
from api_v1.user.repository import UserRepository


@dataclass
class UserService:
    user_repository: UserRepository

    async def get_user(self, user_id: int):
        return await self.user_repository.get_user(user_id)

    async def create_user(self, email: str, password: str):
        user = await self.user_repository.create_user(email=email, password=password)
        return UserLoginSchema(user_id=user.id, access_token="fff")
