# Generated by Django 2.2.28 on 2023-03-23 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dorm_detective_app', '0016_auto_20230323_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 15, 23, 26, 459792, tzinfo=utc)),
        ),
    ]
