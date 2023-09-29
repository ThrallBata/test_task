# Generated by Django 4.2.5 on 2023-09-28 11:16

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewerlesson',
            name='last_view',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 28, 11, 16, 0, 573669, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterUniqueTogether(
            name='viewerlesson',
            unique_together={('lesson', 'user')},
        ),
    ]