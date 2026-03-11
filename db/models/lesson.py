from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP

from .base import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.id", ondelete="CASCADE"), nullable=False
    )
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False
    )
    date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    topic: Mapped[str] = mapped_column(String, nullable=False)

    group: Mapped["Group"] = relationship("Group", back_populates="lessons")

    def __str__(self):
        return f"Lesson(id={self.id}, group_id={self.group_id}, teacher_id={self.teacher_id}, date={self.date}, topic={self.topic})"

    def __repr__(self):
        return f"Lesson(id={self.id}, group_id={self.group_id}, teacher_id={self.teacher_id}, date={self.date}, topic={self.topic})"
