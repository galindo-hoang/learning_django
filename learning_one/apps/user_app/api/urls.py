from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import register, logout

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]