from sqlalchemy.orm import Session

from db.models import User, Student, UserRole


class StudentService:
    def __init__(self, session: Session):
        self.session = session

    def create_student(self, user: User, first_name: str, last_name: str, phone: str) -> Student:
        if user.role != UserRole.STUDENT:
            raise ValueError('user role is not student')
        if user.student_profile:
            raise ValueError('student already exists.')
        
        student = Student(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            user=user
        )
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)

        return student
    