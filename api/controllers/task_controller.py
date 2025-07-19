from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import TaskSerializer
from core.utils import print_error_details
from api.services.task_service import TaskService
from api.services.category_service import CategoryService

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


            task = TaskService.add_task(data.get('user_id'), data.get('title'), data.get('description'), data.get('category_id'))
            if not task:
                return Response({'error': 'Task not created!'}, status=status.HTTP_400_BAD_REQUEST)


            serializer = TaskSerializer(task)
            return Response(
                {
                    'message': 'Task successfully created!',
                    'task': serializer.data
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['DELETE'])
    def detele_task(request):
        try:
            data = request.data

            if data.get('task_id') is None or data.get('task_id') == '':
                return Response({'error': 'Task ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            task = TaskService.delete_task(data.get('task_id'))
            if not task:
                return Response({'error': 'Task not deleted!'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Task successfully deleted!'}, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['GET'])
    def get_all_tasks(request):
        try:
            tasks = TaskService.get_all_tasks()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['GET'])
    def get_tasks_by_user_email(request):
        try:
            email = request.GET.get('email')
            page_number = request.GET.get('page_number')
            filter = request.GET.get('filter')
            search_term = request.GET.get('search_term')
            category_id = request.GET.get('category_id')

            if email is None or email == '':
                return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

            tasks, amount_of_tasks = TaskService.get_tasks_by_user_email(email, page_number, filter, search_term, category_id)
            serializer = TaskSerializer(tasks, many=True)
            return Response({'tasks': serializer.data, 'amount_of_tasks': amount_of_tasks}, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['DELETE'])
    def delete_task(request):
        try:
            data = request.data
            if not TaskService.delete_task(data.get('task_id')):
                return Response({'error': 'Task not deleted!'}, status=400)

            return Response({'message': 'Task successfully deleted!'}, status=200)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=500)

    @staticmethod
    @api_view(['PUT'])
    def update_task_status(request):
        try:
            data = request.data

            if data.get('task_id') is None or data.get('task_id') == '':
                return Response({'error': 'Task ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            if data.get('status') is None or data.get('status') == '':
                return Response({'error': 'Status is required'}, status=status.HTTP_400_BAD_REQUEST)

            task = TaskService.update_task_status(data.get('status'), data.get('task_id'))
            if not task:
                return Response({'error': 'Task not updated!'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Task successfully updated!'}, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['PUT'])
    def update_task_infos(request):
        try:
            data = request.data

            if data.get('task_id') is None or data.get('task_id') == '':
                return Response({'error': 'Task ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            if data.get('title') is None or data.get('title') == '':
                return Response({'error': 'Title is required'}, status=status.HTTP_400_BAD_REQUEST)

            if data.get('description') is None or data.get('description') == '':
                return Response({'error': 'Description is required'}, status=status.HTTP_400_BAD_REQUEST)

            task = TaskService.update_task_infos(data.get('task_id'), data.get('title'), data.get('description'))

            serializer = TaskSerializer(task)

            if not task:
                return Response({'error': 'Task not updated!'}, status=status.HTTP_400_BAD_REQUEST)

            return Response(
                {
                    'message': 'Task successfully updated!',
                    'task': serializer.data
                }, status=status.HTTP_200_OK
            )
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)