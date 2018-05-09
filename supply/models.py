from django.db import models
from django.contrib.gis.db import models as geo_models
from django.utils.translation import ugettext_lazy as _

from .validators import validate_phonenumber, validate_service_price


# Create your models here.


class Supplier(models.Model):
    title = models.CharField(_('Название'), max_length=60, unique=True)
    email = models.EmailField(_('Почта'))
    phone_number = models.CharField(_('Номер телефона'), max_length=30,
                                    validators=[validate_phonenumber])
    address = models.CharField(_('Адрес центрального офиса'), max_length=120)

    class Meta:
        verbose_name = _('Поставщик')
        verbose_name_plural = _('Поставщики')

    def __str__(self):
        return self.title


class ServiceArea(models.Model):
    title = models.CharField(_('Название области'), max_length=120,
                             unique=True)
    poly = geo_models.PolygonField(_('Область'), null=True, srid=4326)
    supplier = models.ForeignKey(Supplier, related_name='areas',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Сервисная зона')
        verbose_name_plural = _('Сервисные зоны')

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(_('Название услуги'), max_length=120)
    price = models.CharField(_('Цена услуги'), max_length=60,
                             validators=[validate_service_price])
    service_area = models.ForeignKey(ServiceArea, related_name='services',
                                     on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def __str__(self):
        return '%s: %s' % (self.title, self.price)
