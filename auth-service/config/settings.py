from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN: str = "TOKEN"