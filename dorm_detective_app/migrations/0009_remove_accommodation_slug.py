# Generated by Django 2.2.28 on 2023-03-20 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dorm_detective_app', '0008_auto_20230320_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='slug',
        ),
    ]