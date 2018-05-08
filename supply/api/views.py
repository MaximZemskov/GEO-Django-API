from django.contrib.gis.geos import Point
from django.db.models import Prefetch

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)

from supply.models import (
    Supplier,
    ServiceArea,
    Service
)
from .serializers import (
    # SUPPLIER
    SupplierSerializer,

    # SERVICE AREA
    ServiceAreaSerializer,

    # SERVICE
    ServiceSerializer,

    # SUPPLIER SELECTION
    SupplierSelectionSerializer,
)


# SUPPLIER


class SupplierDetailApiView(RetrieveAPIView, DestroyAPIView,
                            RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierListApiView(ListAPIView, CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    search_fields = ['title']


# SERVICE AREA

class ServiceAreaDetailApiView(RetrieveAPIView, DestroyAPIView,
                               RetrieveUpdateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaListApiView(ListAPIView, CreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    search_fields = ['title']


# SERVICE

class ServiceDetailApiView(RetrieveAPIView, DestroyAPIView,
                           RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceListApiView(ListAPIView, CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    search_fields = ['title']


# SUPPLIER SELECTION

class SupplierSelectionListApiView(ListAPIView):
    serializer_class = SupplierSelectionSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('x', None)
        longitude = self.request.query_params.get('y', None)
        service_title = self.request.query_params.get('title', None)

        self.queryset = []

        try:
            point = Point(float(latitude), float(longitude), srid=4326) if \
                latitude and longitude else None
        except ValueError:
            point = None

        filter_params = {
            'areas__poly__intersects': point,
            'areas__services__title': service_title
        }
        filter_params = {
            k: v for k, v in filter_params.items()
            if v is not None
        }

        inner_filter_params = []
        if point:
            inner_filter_params += (
                Prefetch('areas',
                         queryset=ServiceArea.objects.
                         filter(poly__intersects=point)),)
        if service_title and not point:
            inner_filter_params += (
                Prefetch('areas',
                         queryset=ServiceArea.objects.
                         filter(services__title=service_title)),)
        if service_title:
            inner_filter_params += (
                Prefetch('areas__services',
                         queryset=Service.objects.
                         filter(title=service_title)),)

        if point and service_title:
            inner_filter_params = (
                Prefetch('areas', queryset=ServiceArea.objects.
                         filter(poly__intersects=point,
                                services__title=service_title)
                         ),
                Prefetch('areas__services', queryset=Service.objects.
                         filter(title=service_title))
            )

        if filter_params:
            self.queryset = Supplier.objects.prefetch_related(
                *inner_filter_params).filter(**filter_params).distinct()

        return self.queryset
