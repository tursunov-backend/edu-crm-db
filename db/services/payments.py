from sqlalchemy.orm import Session

from ..models import Student, Payment, Group


class PaymentService:
    def __init__(self, session: Session):
        self.session = session

    def make_payment(self, student: Student, group: Group, amount: float):
        payment = Payment(student_id=student.id, group_id=group.id, amount=amount)
        self.session.add(payment)
        self.session.commit()

        return payment

    def refund_payment(self, payment: Payment):
        existing_payment = self.get_payment_by_id(payment.id)
        if not existing_payment:
            raise ValueError("Payment not found.")

        self.session.delete(existing_payment)
        self.session.commit()

    def get_payment_by_id(self, id: int) -> Payment:
        return self.session.query(Payment).filter_by(id=id).first()
