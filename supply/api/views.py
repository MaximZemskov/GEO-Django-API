from django.db.models import Q

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
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from supply.models import (
    Supplier,
    ServiceArea,
)

from .pagination import (
    SupplierLimitOffsetPagination,
    SupplierPageNumberPagination,
)

from .serializers import (
    # SUPPLIER
    SupplierCreateSerializer,
    SupplierDetailSerializer,
    SupplierListSerializer,

    # SERVICE AREA
    ServiceAreaSerializer,
)


# SUPPLIER

class SupplierCreateApiView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierCreateSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class SupplierDetailApiView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierDetailSerializer


class SupplierDeleteApiView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierDetailSerializer


class SupplierUpdateApiView(RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)


class SupplierListApiView(ListAPIView):
    serializer_class = SupplierListSerializer
    pagination_class = SupplierLimitOffsetPagination # PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Supplier.objects.all()
        return queryset_list


# SERVICE AREA

# class ServiceAreaCreateApiView(CreateAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


class ServiceAreaDetailApiView(RetrieveAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


# class ServiceAreaDeleteApiView(DestroyAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierDetailSerializer

#
# class ServiceAreaUpdateApiView(RetrieveUpdateAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierDetailSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     # def perform_update(self, serializer):
#     #     serializer.save(user=self.request.user)


class ServiceAreaListApiView(ListAPIView):
    serializer_class = ServiceAreaSerializer
    pagination_class = SupplierLimitOffsetPagination  # PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']

    def get_queryset(self, *args, **kwargs):
        queryset_list = ServiceArea.objects.all()
        return queryset_list




