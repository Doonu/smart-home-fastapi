from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from config.base_model import Base


class User(Base):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
