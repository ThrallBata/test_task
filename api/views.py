from django.db.models import Sum, FilteredRelation, Q, F


from rest_framework import viewsets, status, mixins, exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserLessonsSerializer, ProductLessonsSerializer
from .models import ViewerLesson, Product, User, ProductAccess, Lesson


USER_ID = 1


def get_product_accesses(user):
    return ProductAccess.objects.filter(
            user=user,
            is_valid=True)


class UserLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserLessonsSerializer

    def get_queryset(self):
        # TODO передача USER_ID с помощью выбранного способа аутентификации

        accesses = get_product_accesses(USER_ID)

        queryset = Lesson.objects.filter(
            products__in=accesses.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=USER_ID)
            )
        ).annotate(
            status=F('view_info__status'),
            duration_view=F('view_info__duration_view')
        )

        return queryset


class ProductLessonsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductLessonsSerializer

    def get_queryset(self):
        product_id = self.request.data.get('product_id')
        accesses = get_product_accesses(USER_ID)

        if not (int(product_id) in accesses.values_list('product_id', flat=True)):
            raise exceptions.NotFound

        queryset = Lesson.objects.filter(
            products=product_id
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=USER_ID)
            )
        ).annotate(
            status=F('view_info__status'),
            duration_view=F('view_info__duration_view'),
            last_view=F('view_info__last_view')
        )

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
