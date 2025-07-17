from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task
from django.contrib.auth.hashers import make_password, check_password
from core.utils import print_error_details

# Create your views here.

@api_view(['GET'])
def get_all_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        print_error_details(e)
        return Response({'error': 'Internal Server Error'}, status=500)

@api_view(['GET'])
def get_user_by_email(request):
    email = request.GET.get('email')

    if email is None or email == '':
        return Response({'error': 'Email is required'}, status=400)

    try:
        User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    try:
        user = User.objects.get(email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except Exception as e:
        print_error_details(e)
        return Response({'error': 'Internal Server Error'}, status=500)


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

        if User.objects.filter(email=data.get('email')).exists():
            return Response({'error': 'User already exists'}, status=400)


        pasword_hash = make_password(data.get('password'))

        new_user = User(
            name=data.get('name'),
            email=data.get('email'),
            password_hash=pasword_hash
        )

        new_user.save()

        return Response({'message': 'user successfully created!'}, status=200)
    except Exception as e:
        print_error_details(e)
        return Response({'error': 'Internal Server Error'}, status=500)