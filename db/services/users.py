from sqlalchemy.orm import Session

from ..models import User, UserRole
from db.utils.hashing import hash_password


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def register(self, username: str, password: str, role) -> User:
        existing_user = self.get_user_by_username(username=username)

        if existing_user:
            raise ValueError("username already exist.")

        if role not in (UserRole.ADMIN, UserRole.TEACHER, UserRole.STUDENT):
            raise ValueError("role doesn't exist.")

        user = User(
            username=username, hashed_password=hash_password(password), role=role
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def valid_password(self, user: User, password: str) -> bool:
        return user.hashed_password == hash_password(password)

    def auth(self, username: str, password: str, role) -> User:
        user = self.get_user_by_username(username)
        if not user:
            return None

        if self.valid_password(user, password):
            return user

    def get_user_by_username(self, username: str) -> User:
        user = self.session.query(User).filter_by(username=username).first()
        return user
