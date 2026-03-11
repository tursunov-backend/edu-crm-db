from sqlalchemy.orm import Session

from ..models import Group, Course, Enrollment, Student, GroupStatus


class GroupService:
    def __init__(self, session: Session):
        self.session = session

    def create_group(self, course: Course, name: str, capacity: int) -> Group:
        group = Group(
            course_id=course.id,
            name=name,
            capacity=capacity,
            status=GroupStatus.ACTIVE,
        )

        self.session.add(group)
        self.session.commit()
        self.session.refresh(group)

        return group

    def update_group(
        self, group: Group, capacity: int = None, status: GroupStatus = None
    ) -> Group:
        if capacity is not None and capacity < 0:
            raise ValueError("Capacity cannot be negative")
        if status is not None:
            if status not in (
                GroupStatus.PANDING,
                GroupStatus.ACTIVE,
                GroupStatus.CLOSED,
                GroupStatus.GRADUATED,
            ):
                raise ValueError("Invalid group status")

        group.capacity = capacity
        group.status = status

        self.session.commit()
        self.session.refresh(group)

        return group

    def add_student(self, student: Student, group: Group):
        if group.capacity <= 0:
            raise ValueError("Group is full.")

        existing_enrollment = self.get_enrollment(student, group)
        if existing_enrollment:
            raise ValueError("Student is already enrolled in this group.")

        enrollment = Enrollment(student_id=student.id, group_id=group.id)
        self.session.add(enrollment)
        group.capacity -= 1
        self.session.commit()

    def remove_student(self, student: Student, group: Group):
        enrollment = self.get_enrollment(student, group)
        if not enrollment:
            raise ValueError("Student is not enrolled in this group.")

        self.session.delete(enrollment)
        group.capacity += 1
        self.session.commit()

    def get_group_by_id(self, id: int) -> Group:
        return self.session.query(Group).filter_by(id=id).first()

    def get_enrollment(self, student: Student, group: Group):
        return (
            self.session.query(Enrollment)
            .filter_by(student_id=student.id, group_id=group.id)
            .first()
        )
