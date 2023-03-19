# Generated by Django 2.2.28 on 2023-03-16 01:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm_detective_app', '0002_auto_20230309_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(default='Description', max_length=2048)),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=8, validators=[django.core.validators.MaxValueValidator(90.0), django.core.validators.MinValueValidator(-90.0)])),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9, validators=[django.core.validators.MaxValueValidator(180.0), django.core.validators.MinValueValidator(-180.0)])),
                ('rent_min', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('rent_max', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('avg_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(1.0)])),
                ('reviews_no', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm_detective_app.University')),
            ],
            options={
                'unique_together': {('university', 'name')},
            },
        ),
    ]