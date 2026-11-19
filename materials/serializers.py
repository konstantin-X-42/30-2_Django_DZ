from rest_framework import serializers
from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        # 30.1 связываем сериализатор с моделью курса
        model = Course
        # 30.1 включаем все поля модели курса в JSON-представление
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        # 30.1 связываем сериализатор с моделью урока
        model = Lesson
        # 30.1 включаем все поля модели урока в JSON-представление
        fields = '__all__'
