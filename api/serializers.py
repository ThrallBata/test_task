from rest_framework import serializers
from .models import ViewerLesson, Lesson, Product


class UserLessonsSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    duration_view = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('name', 'status', 'duration_view')


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'viewers',)


class ProductLessonsSerializer(serializers.ModelSerializer):

    lesson = LessonsSerializer(many=True, read_only=True, source='lessons')

    class Meta:
        model = Product
        fields = ('name', 'lesson')

