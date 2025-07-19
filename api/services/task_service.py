from api.repositories.task_repository import TaskRepository
from api.models.task import Task
from api.models.category import Category

class TaskService:
    @staticmethod
    def add_task(user_id: int, title: str, description: str, category_id: int = None) -> Task:
        return TaskRepository.add_task(user_id, title, description, category_id)

    @staticmethod
    def delete_task(task_id: int):
        return TaskRepository.delete_task(task_id)

    @staticmethod
    def update_task_status(status: bool, task_id: int) -> Task:
        return TaskRepository.update_task_status(status, task_id)

    @staticmethod
    def update_task_infos(task_id: int, title: str, description: str) -> Task:
        return TaskRepository.update_task_infos(task_id, title, description)

    @staticmethod
    def get_tasks_by_user_email(email: str, page_number: int, filter: str, search_term: str, category_id: int) -> list[Task]:
        return TaskRepository.get_tasks_by_user_email(email, page_number, filter, search_term, category_id)

    @staticmethod
    def get_all_tasks() -> list[Task]:
        return TaskRepository.get_all_tasks()