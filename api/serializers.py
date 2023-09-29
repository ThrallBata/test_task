from rest_framework import serializers
from .models import ViewerLesson, Lesson, Product


class UserLessonsSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    duration_view = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('name', 'status', 'duration_view')


class ProductLessonsSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    duration_view = serializers.IntegerField()
    last_view = serializers.DateTimeField()

    class Meta:
        model = Lesson
        fields = ('name', 'status', 'duration_view', 'last_view')


