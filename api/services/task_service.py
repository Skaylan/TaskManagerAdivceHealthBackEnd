from api.repositories.task_repository import TaskRepository
from api.models.task import Task
class TaskService:
    @staticmethod
    def add_task(user_id: int, title: str, description: str) -> Task:
        return TaskRepository.add_task(user_id, title, description)

    @staticmethod
    def delete_task(task_id: int):
        return TaskRepository.delete_task(task_id)

    @staticmethod
    def update_task_status(status: bool, task_id: int) -> Task:
        return TaskRepository.update_task_status(status, task_id)

    @staticmethod
    def update_task_infos(task_id: int, title: str, description: str) -> Task:
        return TaskRepository.update_task_infos(task_id, title, description)