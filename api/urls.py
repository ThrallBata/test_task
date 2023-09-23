from django.urls import path, include
from rest_framework import routers

from .views import UserLessonsViewSet


router = routers.SimpleRouter()
router.register(r'lessons', UserLessonsViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),

]
