from django.urls import path, include
from rest_framework import routers

from .views import UserLessonsViewSet, ProductLessonsViewSet, ProductStatisticsViewSet

router = routers.SimpleRouter()
router.register('lessons', UserLessonsViewSet, 'lessons')
router.register('product', ProductLessonsViewSet, 'product')
router.register('statistics', ProductStatisticsViewSet, 'statistics')

urlpatterns = [
    path('v1/', include(router.urls)),
]
