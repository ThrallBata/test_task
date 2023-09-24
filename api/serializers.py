from rest_framework import serializers
from .models import ViewerLesson, Lesson, Product


class UserLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewerLesson
        fields = ('lesson_id', 'duration_view', 'status', 'last_view')


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'viewers',)


class ProductLessonsSerializer(serializers.ModelSerializer):

    lesson = LessonsSerializer(many=True, read_only=True, source='lessons')

    class Meta:
        model = Product
        fields = ('name', 'lesson')

