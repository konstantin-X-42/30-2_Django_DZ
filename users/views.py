from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    # 30.1 указываем сериализатор для просмотра и обновления профиля пользователя
    serializer_class = UserSerializer
    # 30.1 передаем набор всех пользователей для возможности редактирования любого профиля по ID
    queryset = User.objects.all()
