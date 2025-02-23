from fastapi import APIRouter

from .schema import AuthBase

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=AuthBase)
async def login():
    pass
