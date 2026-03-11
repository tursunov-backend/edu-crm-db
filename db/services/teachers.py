from datetime import date

from sqlalchemy.orm import Session
from sqlalchemy import select, join

from db.services.lessons import LessonService

from ..models import User, Teacher, UserRole, Group, Lesson


class TeacherService:
    def __init__(self, session: Session):
        self.session = session

    def create_teacher(
        self,
        user: User,
        first_name: str,
        last_name: str,
        email: str,
        specialization: str,
    ):
        if user.role != UserRole.TEACHER:
            raise ValueError("user role is not teacher")
        if user.teacher_profile:
            raise ValueError("teacher already exists.")

        teacher = Teacher(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            specialization=specialization,
        )
        self.session.add(teacher)
        self.session.commit()
        self.session.refresh(teacher)

        return teacher

    def assign_group(self, group: Group, teacher: Teacher) -> Group:

        if group.teacher_id:
            raise ValueError("Group already assigned")

        group.teacher_id = teacher.id

        self.session.commit()
        self.session.refresh(group)

        return group

    def view_groups(self, teacher: Teacher) -> list[Group]:
        stmt = select(Group).join(Teacher, Group.teacher_id == teacher.id)

        self.session.execute(stmt).scalars().all()

    def create_lesson(
        self, group: Group, teacher: Teacher, date: date, topic: str = None
    ) -> Lesson:
        lesson_service = LessonService(session=self.session)
        existing_lesson = lesson_service.get_lesson_by_date(
            group_id=group.id, date=date
        )

        if existing_lesson:
            raise ValueError("Lesson already scheduled for this date.")

        if group.teacher_id != teacher.id:
            raise ValueError("Teacher is not assigned to this group.")

        lesson = Lesson(
            group_id=group.id, teacher_id=teacher.id, date=date, topic=topic
        )
        self.session.add(lesson)
        self.session.commit()
        return lesson
