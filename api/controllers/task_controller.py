from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializer, TaskSerializer
from api.models import User, Task
from django.contrib.auth.hashers import make_password, check_password
from core.utils import print_error_details
from api.services.task_service import TaskService


class TaskController:
    @staticmethod
    @api_view(['POST'])
    def add_task(request):
        try:
            data = request.data

            if data.get('user_id') is None or data.get('user_id') == '':
                return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            if data.get('title') is None or data.get('title') == '':
                return Response({'error': 'Title is required'}, status=status.HTTP_400_BAD_REQUEST)

            if data.get('description') is None or data.get('description') == '':
                return Response({'error': 'Description is required'}, status=status.HTTP_400_BAD_REQUEST)

            task = TaskService.add_task(data.get('user_id'), data.get('title'), data.get('description'))
            if not task:
                return Response({'error': 'Task not created!'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Task successfully created!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)