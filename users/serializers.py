from rest_framework import serializers
# 30.2 импортируем модель Payment для создания сериализатора платежей
from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        # 30.2 связываем сериализатор с моделью платежей
        model = Payment
        # 30.2 включаем все поля модели платежей в JSON-представление
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # 30.2 добавляем вывод списка всех платежей пользователя через обратную связь related_name='payments'
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        # 30.1 связываем сериализатор с кастомной моделью пользователя
        model = User
        # 30.2 добавляем поле payments в профиль пользователя для просмотра истории оплат
        fields = ('id', 'email', 'phone', 'city', 'avatar', 'first_name', 'last_name', 'payments')


#------до доработки доп 30,2----------------


# from rest_framework import serializers
# # 30.2 импортируем модель Payment для создания сериализатора платежей
# from users.models import User, Payment
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         # 30.1 связываем сериализатор с кастомной моделью пользователя
#         model = User
#         # 30.1 определяем поля профиля пользователя, доступные для просмотра и редактирования
#         fields = ('id', 'email', 'phone', 'city', 'avatar', 'first_name', 'last_name')
#
#
# class PaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         # 30.2 связываем сериализатор с моделью платежей
#         model = Payment
#         # 30.2 включаем все поля модели платежей в JSON-представление
#         fields = '__all__'


#-------30.1-----

# from rest_framework import serializers
# from users.models import User
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         # 30.1 связываем сериализатор с кастомной моделью пользователя
#         model = User
#         # 30.1 определяем поля профиля пользователя, доступные для просмотра и редактирования
#         fields = ('id', 'email', 'phone', 'city', 'avatar', 'first_name', 'last_name')
