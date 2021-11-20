from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Cities(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название Города')
    lt = models.FloatField(verbose_name='Широта')
    lg = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Города'
        ordering = ('name',)


class Locations(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='Названия места'
    )
    city = models.ForeignKey(
        Cities,
        on_delete=models.SET_NULL,
        verbose_name='Город',
        null=True
    )
    lt = models.FloatField(verbose_name='Широта')
    lg = models.FloatField(verbose_name='Долгота')
    description = models.CharField(max_length=512, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Места'
        ordering = ('name',)


class Pictures(models.Model):
    name = models.CharField(
        default='Unnamed picture',
        max_length=50,
        verbose_name='Название фотографии'
    )
    location = models.ForeignKey(
        Locations,
        on_delete=models.SET_NULL,
        verbose_name='Место',
        null=True
    )
    img = models.ImageField(verbose_name='Фото', null=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фотографии'
