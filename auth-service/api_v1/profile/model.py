from sqlalchemy import String, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import TYPE_CHECKING

from config import Base

if TYPE_CHECKING:
    from api_v1.user.model import User


class Profile(Base):
    email: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    gender: Mapped[int] = mapped_column(
        Integer, CheckConstraint("gender IN (1, 2)"), nullable=True
    )

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), unique=True, nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="profile")
