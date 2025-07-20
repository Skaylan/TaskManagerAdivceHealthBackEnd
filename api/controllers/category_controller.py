from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.utils import print_error_details
from api.services.category_service import CategoryService
from api.serializers import CategorySerializer
from api.services.user_service import UserService
class CategoryController:

    @staticmethod
    @api_view(['POST'])
    def create_category(request):
        try:
            data = request.data

            if not data.get('name') or data.get('name') == '':
                return Response({'error': 'Category name is required'}, status=status.HTTP_400_BAD_REQUEST)

            user = UserService.get_user_by_email(data.get('email'))
            category = CategoryService.create_category(data.get('name'), user)
            if not category:
                return Response({'error': 'Category not created!'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = CategorySerializer(category)

            return Response(
                {
                    'message': 'Category successfully created!',
                    'category': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['GET'])
    def get_user_categories_by_email(request):
        try:
            email = request.GET.get('email')

            if not email or email == '':
                return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

            user = UserService.get_user_by_email(email)
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            user = UserService.get_user_by_email(email)

            categories = CategoryService.get_user_categories(user)
            serializer = CategorySerializer(categories, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    @api_view(['DELETE'])
    def delete_category(request):
        try:
            #delete category
            data = request.data

            if not data.get('category_id') or data.get('category_id') == '':
                return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            if not CategoryService.delete_category(data.get('category_id')):
                return Response({'error': 'Category not deleted!'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Category successfully deleted!'}, status=status.HTTP_200_OK)
        except Exception as e:
            print_error_details(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

