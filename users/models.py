from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # 30.1 отключаем стандартное поле username, так как авторизация будет происходить по email
    username = None

    # 30.1 переопределяем поле email, делая его уникальным для использования в качестве логина
    email = models.EmailField(
        unique=True,
        verbose_name='Почта',
        help_text='Укажите почту'
    )

    # 30.1 добавляем необязательное поле для номера телефона пользователя
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name='Телефон',
        help_text='Укажите телефон'
    )

    # 30.1 добавляем необязательное поле для города проживания пользователя
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Укажите город'
    )

    # 30.1 добавляем необязательное поле для загрузки аватара пользователя
    avatar = models.ImageField(
        upload_to='users/avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар',
        help_text='Загрузите аватар'
    )

    # 30.1 устанавливаем поле email в качестве основного идентификатора при входе в систему
    USERNAME_FIELD = 'email'

    # 30.1 убираем обязательные дополнительные поля при создании суперпользователя через консоль
    REQUIRED_FIELDS = []

    class Meta:
        # 30.1 задаем человекочитаемые названия модели в единственном и множественном числе для админки
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        # 30.1 возвращаем email пользователя при строковом представлении объекта
        return self.email
