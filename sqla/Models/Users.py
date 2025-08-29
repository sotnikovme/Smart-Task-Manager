from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, validates, declared_attr, relationship

from sqla.Models.Base import Base
# from sqla.Models.Tasks import Task

class User(Base):

    __tablename__ = "users"

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]  = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    reg_data: Mapped[Optional[datetime]] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    tasks: Mapped[List["Task"]] = relationship(back_populates="user", uselist=True)

    @validates('password')
    def validate_password(self, password):
        if len(password)<8:
            raise ValueError("password length must be more than 8 characters")
        return password