from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    ECHO: bool = False


app_settings = Settings()
