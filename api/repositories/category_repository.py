from api.models.category import Category
from core.utils import print_error_details
from api.models.user import User
class CategoryRepository:
    @staticmethod
    def create_category(name: str, user: User) -> Category:
        try:
            new_category = Category(name=name, user=user)
            new_category.save()
            return new_category
        except Exception as e:
            print_error_details(e)

    @staticmethod
    def get_category_by_id(id: int) -> Category:
        try:
            return Category.objects.get(id=id)
        except Exception as e:
            print_error_details(e)


    @staticmethod
    def get_user_categories(user: User) -> list[Category]:
        try:
            return Category.objects.filter(user=user)
        except Exception as e:
            print_error_details(e)