from django.urls import path, include
from rest_framework import routers

from .views import UserLessonsViewSet, ProductLessonsViewSet, ProductStatisticsAPIView

router = routers.SimpleRouter()
router.register('lessons', UserLessonsViewSet, 'lessons')
# router.register(r'product', ProductLessonsViewSet)

urlpatterns = [
    # path('v1/products/statistics/', ProductStatisticsAPIView),
    path('v1/', include(router.urls)),
]
