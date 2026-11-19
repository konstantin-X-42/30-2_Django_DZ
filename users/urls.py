# users/urls.py
from django.urls import path
from users.apps import UsersConfig
from users.views import UserUpdateAPIView

# 30.1 задаем пространство имен приложения users
app_name = UsersConfig.name

urlpatterns = [
    # 30.1 маршрут для получения и редактирования профиля любого пользователя по ID (GET, PUT, PATCH)
    path('users/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
]
