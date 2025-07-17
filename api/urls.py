from django.urls import path
from . import views

urlpatterns = [
    path('get_all_users', views.get_all_users, name='get_all_users'),
    path('get_user_by_email', views.get_user_by_email, name='get_user_by_email'),
    path('create_user', views.create_user, name='create_user'),
]