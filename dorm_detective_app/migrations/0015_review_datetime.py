# Generated by Django 2.2.28 on 2023-03-23 13:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dorm_detective_app', '0014_university_synopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 13, 17, 43, 396162, tzinfo=utc)),
        ),
    ]
