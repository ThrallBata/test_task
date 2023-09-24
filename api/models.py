from django.utils import timezone

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    duration = models.IntegerField()
    viewers = models.ManyToManyField(User, through='ViewerLesson')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    owners = models.ManyToManyField(User)
    lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.name


class ViewerLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,)
    duration_view = models.IntegerField()

    # if Lesson.objects.filter(viewers=lesson).duration * 0.8 <= int(duration_view):
    #     status_view = "Просмотрено"
    # TODO смена стасуса
    status = models.CharField(max_length=100, default="Не просмотрено")
    last_view = models.DateTimeField(default=timezone.now())
