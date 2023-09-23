from rest_framework import serializers
from .models import ViewerLesson, Lesson


class UserLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewerLesson
        fields = ('user_id', 'duration_view',)


class LessonSerializer(serializers.ModelSerializer):
    # viewerlesson = UserLessonsSerializer(read_only=True, many=True)

    class Meta:
        model = Lesson
        fields = ('name', 'viewers')
        # fields = ('__all__', 'viewerlesson',)
