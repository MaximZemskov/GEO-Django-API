from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models


# Create your models here.


class Supplier(models.Model):
    title = models.CharField('Название', max_length=60, unique=True)
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField('Номер телефона', max_length=15)
    address = models.CharField('Адрес центрального офиса', max_length=120)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title


class ServiceArea(models.Model):
    title = models.CharField('Название области', max_length=120, unique=True)
    poly = geo_models.PolygonField('Область', null=True)
    supplier = models.ForeignKey(Supplier, related_name='areas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сервисная зона'
        verbose_name_plural = 'Сервисные зоны'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=120, unique=True)
    price = models.CharField('Цена услуги', max_length=60)
    service_area = models.ForeignKey(ServiceArea, related_name='services', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return '%s: %s' % (self.title, self.price)

    def __unicode__(self):
        return '%s: %s' % (self.title, self.price)
