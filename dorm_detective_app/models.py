from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class University(models.Model):
    NAME_MAX_LENGTH = 128
    DESCRIPTION_MAX_LENGTH = 2048

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6,
        validators=[
            MaxValueValidator(90.0),
            MinValueValidator(-90.0),
        ],
        default=0,
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[
            MaxValueValidator(180.0),
            MinValueValidator(-180.0),
        ],
        default=0,
    )
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, default="Description")
    picture = models.ImageField(upload_to='university_images', blank=True)
    website = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    current_student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
