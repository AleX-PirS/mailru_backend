from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(
        verbose_name='Биография',
        max_length=500,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True
    )
    interests = models.TextField(
        verbose_name='Интересы',
        max_length=250,
        null=True,
        blank=True
    )
    fav_camera = models.TextField(
        verbose_name='Любимое оборудование',
        max_length=100,
        null=True,
        blank=True)

    def __str__(self):
        return 'Пользователи'
