from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped
from sqlalchemy.testing.schema import mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)


class Task(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
