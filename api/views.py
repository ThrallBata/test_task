from django.db.models import Sum

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserLessonsSerializer, ProductLessonsSerializer
from .models import ViewerLesson, Product, User


class UserLessonsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserLessonsSerializer

    def get_queryset(self):
        queryset = ViewerLesson.objects.select_related('lesson').filter(user=2)
        return queryset


class ProductLessonsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductLessonsSerializer

    def get_queryset(self):
        queryset = Product.objects.prefetch_related('lessons').filter(owners__name='Peter')
        return queryset


@api_view(['GET'])
def ProductStatisticsAPIView(request):
    data = {}
    queryset = Product.objects.prefetch_related('lessons').all()

    for product in queryset:
        viewerlessons = ViewerLesson.objects.filter(lesson_id__in=product.lessons.all()).filter(status='Просмотрено')
        duration_view_sum = (
            ViewerLesson.objects.filter(lesson_id__in=product.lessons.all()).aggregate(Sum('duration_view')))
        user_count = (
            ViewerLesson.objects.filter(lesson_id__in=product.lessons.all()).order_by().values("user").distinct()).count()
        buys_percent = ((user_count / (User.objects.all()).count())) * 100

        dict_product = {'lessons_views': viewerlessons.count(),
                       'duration_view_sum': duration_view_sum['duration_view__sum'],
                       'user_count': user_count,
                       'buys_percent': buys_percent, }

        data[product.id] = dict_product

    return Response(data, status=status.HTTP_200_OK)
