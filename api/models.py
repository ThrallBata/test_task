from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    is_valid = models.BooleanField(default=True)


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class StatusLessonView(models.TextChoices):
    VIEWED = "Просмотрено"
    NO_VIEWED = "Не просмотрено"


class ViewerLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='views')
    duration_view = models.IntegerField()
    status = models.CharField(max_length=100, choices=StatusLessonView.choices, default=StatusLessonView.NO_VIEWED)
    last_view = models.DateTimeField(default=timezone.now())

    class Meta:
        unique_together = ('lesson', 'user')
