from pydantic import BaseModel
from typing import Optional


class AuthBase(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str
