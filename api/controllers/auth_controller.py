import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.utils import print_error_details
from django.contrib.auth.hashers import check_password
from api.services.user_service import UserService
import jwt
from dotenv import load_dotenv

load_dotenv()

class AuthController:
    @staticmethod
    @api_view(['POST'])
    def authenticate(request):
        try:
            data = request.data

            if data.get('email') is None or data.get('email') == '':
                return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

            if data.get('password') is None or data.get('password') == '':
                return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)

            user = UserService.get_user_by_email(data.get('email'))

            if not check_password(data.get('password'), user.password_hash):
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            token = jwt.encode({'email': user.email}, os.getenv('SECRET_KEY'), algorithm='HS256')
            return Response({'message': 'Authenticated', 'token': token}, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)