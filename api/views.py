from rest_framework import viewsets
from django.utils import timezone
from .models import Lesson
from .serializers import UserLessonsSerializer, LessonSerializer


# TODO смена стасуса
class UserLessonsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.prefetch_related('viewers').all()
    print(queryset.dates)
    # for elem in queryset:
    #     print(elem.viewers, 'elem')
    #     for i in elem.viewers.all():
    #         print(i.status)

    # print((queryset[0].viewers))
    serializer_class = LessonSerializer

print(timezone.now())
