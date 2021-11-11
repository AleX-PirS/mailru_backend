from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название Города')
    lt = models.FloatField(verbose_name='Широта')
    lg = models.FloatField(verbose_name='Долгота')


class Locations(models.Model):
    name = models.CharField(max_length=32, verbose_name='Названия места')
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, verbose_name='ID города', null=True)
    lt = models.FloatField(verbose_name='Широта')
    lg = models.FloatField(verbose_name='Долгота')
    description = models.CharField(max_length=512, verbose_name='Описание')


class Pictures(models.Model):
    location = models.ForeignKey(Locations, models.SET_NULL, verbose_name='ID места', null=True)
    img = models.ImageField(verbose_name='Фото', null=True)
