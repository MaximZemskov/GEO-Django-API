import pytest
from rest_framework.test import APIClient
from rest_framework import status

from .fixtures import create_user


@pytest.fixture()
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
        "title": "test",
        "email": "test@example.com",
        "phone_number": "+79999999999",
        "address": "Street 5"
    }
    res = client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_api_create_supplier_without_title(api_client):
    data = {
        "email": "test@example.com",
        "phone_number": "+79999999999",
        "address": "Street 5"
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
        "email": "test@example.com",
        "phone_number": "+79999999999",
        "address": "Street 5"
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
        "title": "Test",
        "email": "test@example.com",
        "phone_number": "+79999999999",
        "address": "Street 5",
        "extra_field": 555,
    }
    res = api_client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_api_create_supplier(api_client):
    data = {
        "title": "Test",
        "email": "test@example.com",
        "phone_number": "+79999999999",
        "address": "Street 5",
    }
    res = api_client.post('/api/suppliers/', data=data)
    assert res.status_code == status.HTTP_201_CREATED
