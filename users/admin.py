from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 30.1 настраиваем отображение полей пользователя в списке объектов административной панели
    list_display = ('id', 'email', 'phone', 'city', 'is_active')
