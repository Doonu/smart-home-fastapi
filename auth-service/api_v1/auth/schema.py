from fastapi.params import Form
from pydantic import BaseModel, EmailStr


class RegistrationRequest(BaseModel):
    email: EmailStr = Form()
    password: str = Form()


class AuthResponse(BaseModel):
    user_id: int
    access_token: str
    refresh_token: str
