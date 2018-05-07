import pytest
from django.utils.crypto import get_random_string

from rest_framework.test import APIClient
from rest_framework import status

from .fixtures import create_user
from .factories import (
    get_random_geo_polygon,
    SupplierFactory,
    ServiceAreaFactory,
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


@pytest.mark.django_db
def test_api_full_update_supplier_anauthhorized(client):
    supplier = SupplierFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string())
    }
    res = client.put('/api/suppliers/{}/'.format(supplier.id), data=data)
    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_api_full_update_supplier(api_client):
    supplier = SupplierFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string())
    }
    res = api_client.put('/api/suppliers/{}/'.format(supplier.id), data=data)
    data['pk'] = res.data['pk']
    data['url'] = res.data['url']
    assert res.status_code == status.HTTP_200_OK
    assert res.data == data


@pytest.mark.django_db
def test_api_title_update_supplier(api_client):
    supplier = SupplierFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
    }
    res = api_client.patch('/api/suppliers/{}/'.format(supplier.id),
                           data=data)
    assert res.status_code == status.HTTP_200_OK
    assert res.data['title'] == data['title']


@pytest.mark.django_db
def test_api_update_supplier_by_extra_field(api_client):
    supplier = SupplierFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
        "email": "{}@example.com".format(get_random_string()),
        "phone_number": "+79999999999",
        "address": "{}".format(get_random_string()),
        "extra_field": "{}".format(get_random_string())
    }
    res = api_client.patch('/api/suppliers/{}/'.format(supplier.id),
                           data=data)
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_api_full_update_service_area_anauthhorized(client):
    service_area = ServiceAreaFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
        "poly": get_random_geo_polygon().geojson,
    }
    res = client.put('/api/service_areas/{}/'.format(service_area.id),
                     data=data)
    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_api_full_update_service_area(api_client):
    service_area = ServiceAreaFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
        "poly": get_random_geo_polygon().geojson,
        "supplier": service_area.supplier.id,
        "services": []
    }
    res = api_client.put('/api/service_areas/{}/'.format(service_area.id),
                         data=data)
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_api_title_update_service_area(api_client):
    service_area = ServiceAreaFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
    }
    res = api_client.patch('/api/service_areas/{}/'.format(service_area.id),
                           data=data)
    assert res.status_code == status.HTTP_200_OK
    assert res.data['properties']['title'] == data['title']


@pytest.mark.django_db
def test_api_update_service_area_by_extra_field(api_client):
    service_area = ServiceAreaFactory.create()

    data = {
        "title": "{}".format(get_random_string()),
        "poly": get_random_geo_polygon().geojson,
        "extra_field": get_random_string()
    }
    res = api_client.patch('/api/service_areas/{}/'.format(service_area.id),
                           data=data)
    assert res.status_code == status.HTTP_200_OK
