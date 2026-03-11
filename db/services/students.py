from sqlalchemy.orm import Session
from sqlalchemy import select, join

from ..models import User, Student, UserRole, Group, Enrollment, Payment, Course


class StudentService:
    def __init__(self, session: Session):
        self.session = session

    def create_student(
        self, user: User, first_name: str, last_name: str, phone: str
    ) -> Student:
        if user.role != UserRole.STUDENT:
            raise ValueError("user role is not student")
        if user.student_profile:
            raise ValueError("student already exists.")

        student = Student(
            first_name=first_name, last_name=last_name, phone=phone, user=user
        )
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)

        return student

    def enroll_group(self, student: Student, group: Group):
        if group.capacity <= 0:
            raise ValueError("Group is full.")

        existing_enrollment = self.get_enrollment(student, group)
        if existing_enrollment:
            raise ValueError("Student is already enrolled in this group.")

        enrollment = Enrollment(student_id=student.id, group_id=group.id)
        self.session.add(enrollment)
        group.capacity -= 1
        self.session.commit()

    def make_payment(self, student: Student, group: Group, amount: float):
        payment = Payment(student_id=student.id, group_id=group.id, amount=amount)
        self.session.add(payment)
        self.session.commit()

        return payment

    def view_courses(self, student: Student) -> list[Course]:
        stmt = (
            select(Course)
            .join(Group, Course.id == Group.course_id)
            .join(Enrollment, Group.id == Enrollment.group_id)
            .where(Enrollment.student_id == student.id)
        )

        return self.session.execute(stmt).scalars().all()

    def get_student_by_id(self, id: int) -> Student:
        return self.session.query(Student).filter_by(id=id).first()

    def get_enrollment(self, student: Student, group: Group):
        return (
            self.session.query(Enrollment)
            .filter_by(student_id=student.id, group_id=group.id)
            .first()
        )
