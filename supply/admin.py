from django.contrib.gis import admin

from .models import Supplier, ServiceArea, Service
# Register your models here.

admin.site.register(Supplier)
admin.site.register(ServiceArea)
admin.site.register(Service)
