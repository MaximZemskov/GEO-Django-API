from django.urls import path

from .views import (
    # SUPPLIER
    SupplierCreateApiView,
    SupplierDetailApiView,
    SupplierDeleteApiView,
    SupplierUpdateApiView,
    SupplierListApiView,

    # SERVICE AREAS
    ServiceAreaListApiView,
    ServiceAreaDetailApiView,
)


app_name = 'api-supply'
urlpatterns = [
    # SUPPLIER
    path('create/', SupplierCreateApiView.as_view(), name='create'),
    path('<int:pk>/edit/', SupplierUpdateApiView.as_view(), name='update'),
    path('<int:pk>/delete/', SupplierDeleteApiView.as_view(), name='delete'),
    path('<int:pk>/', SupplierDetailApiView.as_view(), name='detail'),
    path('', SupplierListApiView.as_view(), name='index'),

    # SERVICE AREAS
    path('service_areas/', ServiceAreaListApiView.as_view(), name='service-area-list'),
    path('service_areas/<int:pk>/', ServiceAreaDetailApiView.as_view(), name='service-area-detail'),
]