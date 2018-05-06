from django.db import models
from django.contrib.gis.db import models as geo_models

from .validators import validate_phonenumber, validate_service_price


# Create your models here.


class Supplier(models.Model):
    title = models.CharField('Название', max_length=60, unique=True)
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField('Номер телефона', max_length=30,
                                    validators=[validate_phonenumber])
    address = models.CharField('Адрес центрального офиса', max_length=120)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title


class ServiceArea(models.Model):
    title = models.CharField('Название области', max_length=120, unique=True)
    poly = geo_models.PolygonField('Область', null=True, srid=4326)
    supplier = models.ForeignKey(Supplier, related_name='areas',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сервисная зона'
        verbose_name_plural = 'Сервисные зоны'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=120, unique=True)
    price = models.CharField('Цена услуги', max_length=60,
                             validators=[validate_service_price])
    service_area = models.ForeignKey(ServiceArea, related_name='services',
                                     on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return '%s: %s' % (self.title, self.price)
