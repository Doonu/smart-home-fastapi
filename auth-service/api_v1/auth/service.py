from dataclasses import dataclass

from api_v1.user import UserLoginSchema


@dataclass
class AuthService:

    async def login(self, email, password) -> UserLoginSchema:
        pass
