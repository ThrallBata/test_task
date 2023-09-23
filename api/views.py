from rest_framework import viewsets
from django.utils import timezone
from .models import Lesson, ViewerLesson
from .serializers import UserLessonsSerializer, LessonSerializer


# TODO смена стасуса
class UserLessonsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ViewerLesson.objects.select_related('lesson').filter(user=1)

    ''' Для упращения используется константа, при различных способах аутентификации user_id можно брать из токена или из request'''

    serializer_class = UserLessonsSerializer

