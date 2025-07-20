from api.models.category import Category
from core.utils import print_error_details
from api.models.user import User
from api.models.task import Task


class CategoryRepository:
    @staticmethod
    def create_category(name: str, user: User, color: str) -> Category:
        try:
            new_category = Category(name=name, user=user, color=color)
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

    @staticmethod
    def delete_category(category_id: int) -> Category:
        try:
            category = Category.objects.get(id=category_id)
            tasks = Task.objects.filter(category_id=category)

            for task in tasks:
                task.category = None
                task.save()

            return Category.objects.filter(id=category_id).delete()
        except Exception as e:
            print_error_details(e)

    @staticmethod
    def update_category(category_id: int, name: str, color: str) -> Category:
        try:
            category = Category.objects.get(id=category_id)
            category.name = name
            category.color = color
            category.save()

            return category
        except Exception as e:
            print_error_details(e)