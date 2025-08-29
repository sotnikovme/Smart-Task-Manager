from datetime import datetime

from sqlalchemy import String, func, Date, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, validates, relationship

from sqla.Models import Base
# from sqla.Models.Users import User
from sqla.Models.Colors import Color

class Task(Base):

    __tablename__ = 'tasks'

    title: Mapped[str]
    body: Mapped[str]
    status: Mapped[str]
    priority: Mapped[str]
    deadline_date: Mapped[datetime] = mapped_column(Date, nullable=True)
    owner: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("task_categories.id"), nullable=True)

    user: Mapped["User"] = relationship(back_populates="tasks", uselist=False, foreign_keys=[owner])

    category: Mapped[list["TaskCategories"]] = relationship(back_populates="task", foreign_keys=[category_id])


class TaskCategories(Base):

    __tablename__ = 'task_categories'

    name: Mapped[str]
    color: Mapped[Color] = mapped_column(String)

    task: Mapped[list["Task"]] = relationship(back_populates="category", foreign_keys="Task.category_id")
