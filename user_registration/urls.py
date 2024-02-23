from django.urls import path
from .views import create_user, register_and_login, profile_view, all_users

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('register-and-login/', register_and_login, name='register_and_login'),
    path('profile/', profile_view, name='profile'),
    path('all-users/', all_users, name='all_users'),
]
