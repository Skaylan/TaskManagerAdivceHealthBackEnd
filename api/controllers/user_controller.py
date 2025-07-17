from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializer, TaskSerializer
from api.models import User, Task
from django.contrib.auth.hashers import make_password, check_password
from core.utils import print_error_details
from api.services.user_service import UserService


class UserController:
    @staticmethod
    @api_view(['GET'])
    def get_all_users(request):
        try:
            users = UserService.get_all_users()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['GET'])
    def get_user_by_email(request):
        email = request.GET.get('email')

        if email is None or email == '':
            return Response({'error': 'Email is required'}, status=400)

        try:
            user = UserService.get_user_by_email(email)
            if not user:
                return Response({'error': 'User not found'}, status=404)

            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=500)

    @staticmethod
    @api_view(['POST'])
    def create_user(request):
        try:
            data = request.data

            if data.get('name') is None:
                return Response({'error': 'Name is required'}, status=400)

            if data.get('email') is None:
                return Response({'error': 'Email is required'}, status=400)

            if data.get('password') is None:
                return Response({'error': 'Password is required'}, status=400)

            if data.get('re_password') != data.get('password'):
                return Response({'error': 'Passwords do not match'}, status=400)


            pasword_hash = make_password(data.get('password'))

            new_user = UserService.create_user(data.get('name'), data.get('email'), pasword_hash)

            if not new_user:
                return Response({'error': 'User not created!'}, status=400)

            return Response({'message': 'user successfully created!'}, status=201)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=500)