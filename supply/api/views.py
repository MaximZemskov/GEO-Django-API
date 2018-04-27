from django.contrib.gis.geos import Point
from django.db.models import Prefetch

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)

from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)

from supply.models import (
    Supplier,
    ServiceArea,
    Service
)

from .pagination import (
    CustomLimitOffsetPagination,
)

from .serializers import (
    # SUPPLIER
    SupplierDetailSerializer,
    SupplierListSerializer,

    # SERVICE AREA
    ServiceAreaSerializer,

    # SERVICE
    ServiceSerializer,

    # SUPPLIER SELECTION
    SupplierSelectionSerializer,
    ServiceAreaSelectionSerializer,
    ServiceSelectionSerializer,
)


# SUPPLIER


class SupplierDetailApiView(RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SupplierListApiView(ListAPIView, CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']


# SERVICE AREA

class ServiceAreaDetailApiView(RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceAreaListApiView(ListAPIView, CreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']


# SERVICE

class ServiceDetailApiView(RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceListApiView(ListAPIView, CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']


# SUPPLIER SELECTION

class SupplierSelectionListApiView(ListAPIView):
    serializer_class = SupplierSelectionSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('x', None)
        longitude = self.request.query_params.get('y', None)
        service_title = self.request.query_params.get('title', None)

        point = Point(float(latitude), float(longitude), srid=4326) if latitude and longitude else None
        if point and service_title:
            queryset = Supplier.objects.prefetch_related('areas__services').filter(
                areas__poly__intersects=point,
                areas__services__title=service_title,
            )
        elif point:
            queryset = Supplier.objects.prefetch_related('areas__services').filter(
                areas__poly__intersects=point
            )
        elif service_title:
            queryset = Supplier.objects.prefetch_related('areas__services').filter(
                areas__services__title=service_title
            )
        else:
            queryset = []
        return queryset

