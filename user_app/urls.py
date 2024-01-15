# user_app/urls.py
from django.urls import path
from .views import RegisterView, UserLoginView, DashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # URL для регистрации пользователя
    path('login/', UserLoginView.as_view(), name='login'),  # URL для входа пользователя
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  # Защищенный URL для просмотра информации пользователя
]
