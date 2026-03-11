from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP

from .base import Base, TimestampMixin


class Payment(Base, TimestampMixin):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)

    student: Mapped["Student"] = relationship("Student", back_populates="payments")
    group: Mapped["Group"] = relationship("Group", back_populates="payments")

    def __repr__(self):
        return f"Payment(id={self.id}, student_id={self.student_id}, group_id={self.group_id}, amount={self.amount})"

    def __repr__(self):
        return f"Payment(id={self.id}, student_id={self.student_id}, group_id={self.group_id}, amount={self.amount})"
