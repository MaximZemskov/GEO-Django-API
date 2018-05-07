from django.contrib.gis import admin
from django.utils.translation import ugettext_lazy as _

from .models import Supplier, ServiceArea, Service


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0


class ServiceAreaAdmin(admin.GeoModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'supplier']}),
        (_('Георграфическая информация'),
         {
             'fields': [
                'poly',
             ],
             'classes': [
                 'collapse'
             ]
         }
         ),
    ]
    inlines = [ServiceInline]


class ServiceAreaInline(admin.StackedInline):
    model = ServiceArea
    extra = 0
    show_change_link = True


class SupplierAdmin(admin.GeoModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (_('Контактная информация'),
         {
             'fields': [
                 'email',
                 'phone_number',
                 'address'
             ],
             'classes': [
                 'collapse'
             ]
         }
         ),
    ]
    inlines = [ServiceAreaInline]


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)
