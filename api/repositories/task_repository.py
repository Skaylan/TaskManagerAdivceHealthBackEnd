from api.models.task import Task
from api.services.user_service import UserService
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from api.models.category import Category
from core.utils import print_error_details


class TaskRepository:

    @staticmethod
    def add_task(user_id: int, title: str, description: str, category_id: int):
        if category_id == '':
            category_id = None
        try:
            new_task = Task(
                user_id=user_id,
                title=title,
                description=description,
                category_id=category_id
            )
            new_task.save()

            return new_task
        except Exception as e:
            print_error_details(e)
    @staticmethod
    def delete_task(task_id: int) -> bool:
        result = Task.objects.filter(id=task_id).delete()
        if result[0] == 0:
            return False
        return True

    @staticmethod
    def update_task_status(status: bool, task_id: int) -> Task:
        task = Task.objects.get(id=task_id)
        task.is_done = status
        task.updated_at = timezone.now()
        task.save()
        return task

    @staticmethod
    def update_task_infos(task_id: int, title: str, description: str) -> Task:
        task = Task.objects.get(id=task_id)
        task.title = title
        task.description = description
        task.updated_at = timezone.now()
        task.save()
        return task

    @staticmethod
    def get_tasks_by_user_email(
        email: str,
        page_number: int,
        filter: str,
        search_term: str,
        category_id: int = None
    ) -> tuple[list[Task], int]:
        user = UserService.get_user_by_email(email)

        queryset = Task.objects.filter(user_id=user.id)

        if filter == 'done':
            queryset = queryset.filter(is_done=True)
        elif filter == 'not-done':
            queryset = queryset.filter(is_done=False)

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) | Q(description__icontains=search_term)
            )

        queryset = queryset.order_by('-created_at')

        paginator = Paginator(queryset, 6)
        amount_of_tasks = paginator.count

        try:
            tasks = paginator.page(page_number)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)

        return tasks, amount_of_tasks

    @staticmethod
    def get_all_tasks() -> list[Task]:
        return Task.objects.all()