from typing import Annotated

from fastapi import APIRouter, Depends

from api_v1.user.dependency import get_user_service
from api_v1.user.schema import UserCreateSchema
from api_v1.user.service import UserService

router = APIRouter()


@router.post("")
async def create_user(
    body: UserCreateSchema,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.create_user(email=body.email, password=body.password)
