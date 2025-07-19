from api.models.category import Category
from api.repositories.category_repository import CategoryRepository
from api.models.user import User
class CategoryService:
    @staticmethod
    def create_category(name: str, user: User) -> Category:
        return CategoryRepository.create_category(name=name, user=user)


    @staticmethod
    def get_category_by_id(id: int) -> Category:
        return CategoryRepository.get_category_by_id(id=id)


    @staticmethod
    def get_user_categories(user: User):
        return CategoryRepository.get_user_categories(user=user)