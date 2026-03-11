from sqlalchemy.orm import Session

from ..models import Course


class CourseService:
    def __init__(self, session: Session):
        self.session = session

    def create_course(self, name: str, description: str, price: int) -> Course:
        existing_course = self.get_course_by_name(name)

        if existing_course:
            raise ValueError("course already exist.")

        course = Course(name=name, description=description, price=price)
        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)

        return course

    def update_course(
        self, course: Course, name: str, description: str, price: int
    ) -> Course:
        existing_course = self.get_course_by_name(name)

        if existing_course and existing_course.id != course.id:
            raise ValueError("course name elready exist")

        course.name = name
        course.description = description
        course.price = price

        self.session.commit()
        self.session.refresh(course)

        return course

    def delete_course(self, course: Course):
        if not course:
            raise ValueError("Course not found")

        self.session.delete(course)
        self.session.commit()
        print("Course deleted successfully.")

    def get_course_by_id(self, id: int) -> Course:
        return self.session.query(Course).filter_by(id=id).first()

    def get_course_by_name(self, name: str) -> Course:
        return self.session.query(Course).filter_by(name=name).first()
