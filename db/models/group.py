from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from .base import Base, TimestampMixin


class GroupStatus:
    PENDING = "ochilyotgan"
    ACTIVE = "aktiv"
    CLOSED = "yopilgan"
    GRADUATED = "bitirgan"


class Group(TimestampMixin, Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    course_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("courses.id"), nullable=False
    )

    teacher_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("teachers.id"), nullable=True
    )

    capacity: Mapped[int] = mapped_column(Integer, default=0)

    status: Mapped[str] = mapped_column(String(30), nullable=False)

    course: Mapped["Course"] = relationship("Course", back_populates="groups")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="groups")

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment", back_populates="group"
    )

    payments: Mapped[list["Payment"]] = relationship(
        "Payment", back_populates="group"
    )

    lessons: Mapped[list["Lesson"]] = relationship(
        "Lesson", back_populates="group"
    )

    def __str__(self):
        return f"Group(id={self.id}, name={self.name}, course_id={self.course_id}, teacher_id={self.teacher_id}, capacity={self.capacity}, status={self.status})"

    def __repr__(self):
        return f"Group(id={self.id}, name={self.name}, course_id={self.course_id}, teacher_id={self.teacher_id}, capacity={self.capacity}, status={self.status})"


class Enrollment(TimestampMixin, Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    student_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("students.id"), nullable=False
    )

    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("groups.id"), nullable=False
    )

    student: Mapped["Student"] = relationship(
        "Student", back_populates="enrollments"
    )

    group: Mapped["Group"] = relationship(
        "Group", back_populates="enrollments"
    )

    def __str__(self):
        return f"Enrollment(id={self.id}, student_id={self.student_id}, group_id={self.group_id})"

    def __repr__(self):
        return f"Enrollment(id={self.id}, student_id={self.student_id}, group_id={self.group_id})"