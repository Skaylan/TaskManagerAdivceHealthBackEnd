from api.models.user import User
from api.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_all_users() -> list[User]:
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def create_user(name: str, email: str, password_hash: str) -> User:
        return UserRepository.create_user(name, email, password_hash)