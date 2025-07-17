from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

@api_view(['GET'])
def get_all_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': 'Internal Server Error'}, status=500)