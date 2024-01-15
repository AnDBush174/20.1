# user_app/urls.py
from django.urls import path
from .views import RegisterView, UserLoginView, DashboardView

urlpatterns = [
    path('register/', RegisterView, name='register'),  # URL для регистрации пользователя
    path('login/', UserLoginView, name='login'),  # URL для входа пользователя
    path('dashboard/', DashboardView, name='dashboard'),  # Защищенный URL для просмотра информации пользователя
]
