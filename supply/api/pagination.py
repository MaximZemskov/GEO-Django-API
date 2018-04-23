from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class SupplierLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class SupplierPageNumberPagination(PageNumberPagination):
    page_size = 2
