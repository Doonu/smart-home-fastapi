from fastapi import APIRouter

from .user.handler import router as user_router
from .session.handler import router as session_router

router = APIRouter()
router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(session_router, prefix="/session", tags=["session"])
