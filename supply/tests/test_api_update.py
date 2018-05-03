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
    data['id'] = res.data['id']
    assert res.status_code == status.HTTP_200_OK
    assert res.data == data


@pytest.mark.django_db
def test_api_title_update_supplier(api_client):
    supplier = SupplierFactory.create()
    data = {
        "title": "{}".format(get_random_string()),
    }
    res = api_client.patch('/api/suppliers/{}/'.format(supplier.id), data=data)
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
    res = api_client.patch('/api/suppliers/{}/'.format(supplier.id), data=data)
    assert res.status_code == status.HTTP_200_OK




