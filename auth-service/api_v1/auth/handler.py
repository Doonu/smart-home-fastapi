from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from .dependency import get_auth_service
from .schema import AuthResponse, RegistrationRequest
from .service import AuthService

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=AuthResponse)
async def login():
    pass


@router.post("/registration", response_model=AuthResponse)
async def registration(
    register_request: RegistrationRequest,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    return await auth_service.registration(register_request=register_request)
