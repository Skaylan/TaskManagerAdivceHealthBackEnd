from api.models import User

class UserRepository:
    @staticmethod
    def get_all_users() -> list[User]:
        return User.objects.all()

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.objects.get(email=email)

    @staticmethod
    def create_user(name: str, email: str, password_hash: str) -> User:
        new_user = User(
            name=name,
            email=email,
            password_hash=password_hash
        )
        new_user.save()
        return new_user