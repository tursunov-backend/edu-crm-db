from datetime import date
from sqlalchemy.orm import Session

from ..models import Lesson, Group, Teacher


class LessonService:
    def __init__(self, session: Session):
        self.session = session

    def schedule_lesson(
        self, group: Group, teacher: Teacher, date: date, topic: str = None
    ) -> Lesson:
        existing_lesson = self.get_lesson_by_date(group_id=group.id, date=date)

        if existing_lesson:
            raise ValueError("Lesson already scheduled for this date.")

        lesson = Lesson(
            group_id=group.id, teacher_id=teacher.id, date=date, topic=topic
        )
        self.session.add(lesson)
        self.session.commit()
        return lesson

    def update_lesson(self, lesson: Lesson, date: date, topic: str) -> Lesson:
        if date:
            existing_lesson = self.get_lesson_by_date(
                group_id=lesson.group_id, date=date
            )
            if existing_lesson and existing_lesson.id != lesson.id:
                raise ValueError("Another lesson is already scheduled for this date.")
            lesson.date = date
        if topic is not None:
            lesson.topic = topic

        self.session.commit()
        return lesson

    def cancel_lesson(self, lesson: Lesson):
        exist_lesson = self.get_lesson_by_id(lesson.id)
        if not exist_lesson:
            raise ValueError("Lesson not found.")

        self.session.delete(lesson)
        self.session.commit()

    def get_lesson_by_date(self, group_id: int, date: date) -> Lesson:
        return (
            self.session.query(Lesson).filter_by(group_id=group_id, date=date).first()
        )

    def get_lesson_by_id(self, id: int) -> Lesson:
        return self.session.query(Lesson).filter_by(id=id).first()
