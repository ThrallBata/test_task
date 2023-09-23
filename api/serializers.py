from rest_framework import serializers
from .models import ViewerLesson, Lesson


class UserLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewerLesson
        fields = ('user_id', 'lesson_id', 'duration_view', 'status', 'last_view')



