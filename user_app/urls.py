from django.urls import path
from .views import register, user_login, dashboard

urlpatterns = [
    path('register/', register, name='register'),  # URL для регистрации пользователя
    path('login/', user_login, name='login'),  # URL для входа пользователя
    path('dashboard/', dashboard, name='dashboard'),  # Защищенный URL для просмотра информации пользователя
]
