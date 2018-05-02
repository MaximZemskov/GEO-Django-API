import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.utils.crypto import get_random_string

from .fixtures import create_user
from .factories import (
    get_random_geo_polygon,
    get_random_service_price,
    SupplierFactory,
    ServiceAreaFactory,
    ServiceFactory,
)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def api_client():
    user = create_user()
    client = APIClient()
    client.force_login(user)
    client.user = user
    return client


def test_api_create_supplier_unauthorized(client):
    data = {
        "title": "{}".format(get_random_string()),
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string())
    }
    res = client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_api_create_supplier_without_title(api_client):
    data = {
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string())
    }
    res = api_client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.data == {
        "title": [
            "This field is required."
        ]
    }


@pytest.mark.django_db
def test_api_create_supplier_with_empty_title(api_client):
    data = {
        "title": "",
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string())
    }
    res = api_client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.data == {
        "title": [
            "This field may not be blank."
        ],
    }


@pytest.mark.django_db
def test_api_create_supplier_with_extra_field(api_client):
    data = {
        "title": "{}".format(get_random_string()),
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string()),
        "extra_field": "{}".format(get_random_string()),
    }
    res = api_client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_api_create_supplier(api_client):
    data = {
        "title": "{}".format(get_random_string()),
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string()),
    }
    res = api_client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_api_create_service_area_unauthorized(client):
    supplier = SupplierFactory.create()

    service_area_data = {
            "services": [],  # empty services
            "title": "{}".format(get_random_string()),
            "poly": get_random_geo_polygon().geojson,
            "supplier": supplier.id
    }
    res = client.post('/api/service_areas/', data=service_area_data)
    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_api_create_service_area_with_empty_services(api_client):
    supplier = SupplierFactory.create()

    service_area_data = {
            "services": [],  # empty services
            "title": "{}".format(get_random_string()),
            "poly": get_random_geo_polygon().geojson,
            "supplier": supplier.id
    }
    res = api_client.post('/api/service_areas/', data=service_area_data)
    assert res.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_api_create_service_area_without_services(api_client):
    supplier = SupplierFactory.create()

    service_area_data = {
            "title": "{}".format(get_random_string()),
            "poly": get_random_geo_polygon().geojson,
            "supplier": supplier.id
    }
    res = api_client.post('/api/service_areas/', data=service_area_data)
    assert res.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_api_create_service_area_with_service(api_client):
    supplier = SupplierFactory.create()

    service_data = {
        "title": "{}".format(get_random_string()),
        "price": "{}".format(get_random_service_price()),
    }

    service_area_data = {
        "services": [service_data],
        "title": "{}".format(get_random_string()),
        "poly": get_random_geo_polygon().geojson,
        "supplier": supplier.id
    }
    res = api_client.post('/api/service_areas/', data=service_area_data)
    assert res.status_code == status.HTTP_201_CREATED
    assert len(res.data['properties']['services']) == 1


@pytest.mark.django_db
def test_api_create_service_area_with_few_services(api_client):
    supplier = SupplierFactory.create()

    service_data = [
        {
            "title": "{}".format(get_random_string()),
            "price": "{}".format(get_random_service_price()),
        }, {
            "title": "{}".format(get_random_string()),
            "price": "{}".format(get_random_service_price()),
        }
    ]

    service_area_data = {
        "services": service_data,
        "title": "{}".format(get_random_string()),
        "poly": get_random_geo_polygon().geojson,
        "supplier": supplier.id
    }
    res = api_client.post('/api/service_areas/', data=service_area_data)
    assert res.status_code == status.HTTP_201_CREATED
    assert len(res.data['properties']['services']) == 2


@pytest.mark.django_db
def test_api_create_srvice_area_with_no_valid_poly_field(api_client):
    supplier = SupplierFactory.create()

    service_area_data = {
        "services": [], # empty services
        "title": "{}".format(get_random_string()),
        "poly": {'polygon': 12312},
        "supplier": supplier.id
    }
    res = api_client.post('/api/service_areas/', data=service_area_data)
    assert res.status_code == status.HTTP_400_BAD_REQUEST
