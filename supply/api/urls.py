from django.urls import path

from .views import (
    # SUPPLIER
    SupplierDetailApiView,
    SupplierListApiView,

    # SERVICE AREAS
    ServiceAreaDetailApiView,
    ServiceAreaListApiView,


    # SERVICE
    ServiceDetailApiView,
    ServiceListApiView,

    # SUPPLIER SELECTION
    SupplierSelectionListApiView,
)


app_name = 'api-supply'
urlpatterns = [
    # SUPPLIER
    path('suppliers/', SupplierListApiView.as_view(), name='suppliers-list'),
    path('suppliers/<int:pk>/', SupplierDetailApiView.as_view(), name='suppliers-detail'),

    # SERVICE AREAS
    path('service_areas/', ServiceAreaListApiView.as_view(), name='service-area-list'),
    path('service_areas/<int:pk>/', ServiceAreaDetailApiView.as_view(), name='service-area-detail'),

    # SERVICE
    path('services/', ServiceListApiView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailApiView.as_view(), name='service-detail'),

    # SUPPLIER SELECTION
    path('selection/', SupplierSelectionListApiView.as_view(), name='selection-list'),
]