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
