from django.urls import path
# from . import views
from api.controllers.user_controller import UserController
from api.controllers.task_controller import TaskController
from api.controllers.auth_controller import AuthController

urlpatterns = [
    path('get_all_users', UserController.get_all_users, name='get_all_users'),
    path('get_user_by_email', UserController.get_user_by_email, name='get_user_by_email'),
    path('create_user', UserController.create_user, name='create_user'),
    path('add_task', TaskController.add_task, name='add_task'),
    path('delete_task', TaskController.delete_task, name='delete_task'),
    path('update_task_status', TaskController.update_task_status, name='update_task_status'),
    path('update_task_infos', TaskController.update_task_infos, name='update_task_infos'),
    path('authenticate', AuthController.authenticate, name='authenticate'),
    path('get_tasks_by_user_email', TaskController.get_tasks_by_user_email, name='get_tasks_by_user_email'),
]