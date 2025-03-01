from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.auth.schema import RegistrationRequest, AuthResponse
from api_v1.auth.utils import hash_password, create_access_token, create_refresh_token
from api_v1.profile.repository import ProfileRepository
from api_v1.profile.schema import ProfileCreateRequest
from api_v1.session.repository import SessionRepository
from api_v1.session.schema import SessionCreate
from api_v1.user.repository import UserRepository
from api_v1.user.schema import UserCreate


@dataclass
class AuthService:
    db_session: AsyncSession
    user_repository: UserRepository
    profile_repository: ProfileRepository
    session_repository: SessionRepository

    async def login(self, email, password) -> AuthResponse:
        pass

    async def registration(self, register_request: RegistrationRequest) -> AuthResponse:
        existing_user = await self.user_repository.get_user_by_email(
            email=register_request.email
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Пользователь с текущим почтовым ящиком уже существует",
            )

        profile_request_data = ProfileCreateRequest(
            email=register_request.email, gender=None
        )
        profile_id = await self.profile_repository.create_profile(
            profile_create=profile_request_data
        )

        hashed_password = await hash_password(password_user=register_request.password)

        user_create_data = UserCreate(
            email=register_request.email,
            password=hashed_password,
            profile_id=profile_id,
        )
        user_id = await self.user_repository.create_user(user_create=user_create_data)

        access_token = await create_access_token(user_id=user_id)
        refresh_token = await create_refresh_token(user_id=user_id)

        session_req = SessionCreate(
            access_token=access_token,
            refresh_token=refresh_token,
            user_id=user_id,
            device_id=register_request.device_id,
        )
        await self.session_repository.create_session(session=session_req)

        return AuthResponse(
            access_token=access_token, refresh_token=refresh_token, user_id=user_id
        )
