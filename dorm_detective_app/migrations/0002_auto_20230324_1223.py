# Generated by Django 2.2.28 on 2023-03-24 12:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dorm_detective_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 12, 23, 25, 657163, tzinfo=utc)),
        ),
    ]
