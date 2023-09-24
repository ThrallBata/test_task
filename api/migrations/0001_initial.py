# Generated by Django 4.2.5 on 2023-09-24 03:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ViewerLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_view', models.IntegerField()),
                ('status', models.CharField(default='Не просмотрено', max_length=100)),
                ('last_view', models.DateTimeField(default=datetime.datetime(2023, 9, 24, 3, 23, 4, 262691, tzinfo=datetime.timezone.utc))),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lessons', models.ManyToManyField(to='api.lesson')),
                ('owners', models.ManyToManyField(to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='viewers',
            field=models.ManyToManyField(through='api.ViewerLesson', to='api.user'),
        ),
    ]
