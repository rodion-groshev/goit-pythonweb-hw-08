from datetime import date
from sqlalchemy import Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    second_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True)
    phone: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    birthday: Mapped[date] = mapped_column(Date)
    additional: Mapped[str] = mapped_column(String)
