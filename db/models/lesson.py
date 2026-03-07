from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP, func

from .base import Base, TimestampMixin
from .user import Teacher, Student
from .group import Group


class Lesson(Base, TimestampMixin):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("groups.id"), nullable=False
    )

    teacher_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("teachers.id"), nullable=False
    )

    topic: Mapped[str] = mapped_column(String(255), nullable=False)

    date: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    group: Mapped["Group"] = relationship("Group", back_populates="lessons")

    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="lessons")
