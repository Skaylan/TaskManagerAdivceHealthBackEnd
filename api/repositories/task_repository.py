from api.models.task import Task
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
        task.save()
        return task