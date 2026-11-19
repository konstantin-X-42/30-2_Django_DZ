from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # 30.1 связываем сериализатор с кастомной моделью пользователя
        model = User
        # 30.1 определяем поля профиля пользователя, доступные для просмотра и редактирования
        fields = ('id', 'email', 'phone', 'city', 'avatar', 'first_name', 'last_name')
