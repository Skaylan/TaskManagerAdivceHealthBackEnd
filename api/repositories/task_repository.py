from api.models.task import Task
from api.services.user_service import UserService
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
class TaskRepository:

    @staticmethod
    def add_task(user_id: int, title: str, description: str):
        new_task = Task(
            user_id=user_id,
            title=title,
            description=description
        )
        new_task.save()
        return new_task

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
    def get_tasks_by_user_email(email: str, page_number: int, filter: str, search_term) -> list[list[Task], int]:
        user = UserService.get_user_by_email(email)
        if filter == 'done':
            task_list = Task.objects.filter(user_id=user.id, is_done=True).order_by('-created_at')
            paginator = Paginator(task_list, 6)
            amount_of_tasks = paginator.count
            try:
                tasks = paginator.page(page_number)
            except PageNotAnInteger:
                tasks = paginator.page(1)
            except EmptyPage:
                tasks = paginator.page(paginator.num_pages)
            return tasks, amount_of_tasks

        if filter == 'not-done':
            task_list = Task.objects.filter(user_id=user.id, is_done=False).order_by('-created_at')
            paginator = Paginator(task_list, 6)
            amount_of_tasks = paginator.count
            try:
                tasks = paginator.page(page_number)
            except PageNotAnInteger:
                tasks = paginator.page(1)
            except EmptyPage:
                tasks = paginator.page(paginator.num_pages)
            return tasks, amount_of_tasks

        if search_term:
            task_list = Task.objects.filter(
                Q(user_id=user.id),
                Q(title__icontains=search_term) | Q(description__icontains=search_term)
            ).order_by('-created_at')

            paginator = Paginator(task_list, 6)
            amount_of_tasks = paginator.count

            try:
                tasks = paginator.page(page_number)
            except PageNotAnInteger:
                tasks = paginator.page(1)
            except EmptyPage:
                tasks = paginator.page(paginator.num_pages)

            return tasks, amount_of_tasks

        task_list = Task.objects.filter(user_id=user.id).order_by('-created_at')
        paginator = Paginator(task_list, 6)
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