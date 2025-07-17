from api.models import Task
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